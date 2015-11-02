console.log("Hello");

var x = require('casper').selectXPath;
casper.options.viewportSize = {width: 1024, height: 574};
casper.on('page.error', function (msg, trace) {
    this.echo('Error: ' + msg, 'ERROR');
    for (var i = 0; i < trace.length; i++) {
        var step = trace[i];
        this.echo('   ' + step.file + ' (line ' + step.line + ')', 'ERROR');
    }
});

casper.test.begin('Login Test', function (test) {
    var loginTester = [
        {
            selector: "form[name=form] input#email",
            action: "sendKeys",
            value: {
                textToEnter: "emailAddress"
            }
        },
        {
            selector: "form[name=form] input#password",
            action: "sendKeys",
            value: {
                textToEnter: "password"
            }
        },
        {
            selector: "[role=login-button]",
            action: "click"
        },
        {
            selector: '[data-ng-click="options.showTags = !(options.showTags || false)"]',
            action: "click"

        },
        {
            action: 'screenshot',
            value: {
                checkUrl: /search$/,
                fileName: '1-searchLanding',
                checkSelector: "[role=action-title]"
            }
        },
        {
            selector: '[data-ng-click="reset()"]',
            action: "reset",
            value: {
                checkSelector: 'ng-pluralize'
            }
        },
        {

            selector: 'input#search-all',
            action: "sendKeys",
            value: {
                textToEnter: 'smith'
            }
        },
        {
            selector: '[data-ng-click="search()"]',
            action: "search",
            value: {
                checkSelector: 'ng-pluralize',
                checkUrl: /all/
            }
        },
        {
            action: 'screenshot',
            value: {
                checkUrl: /provider_last_name_legal_name/,
                fileName: '2-searchAll',
                checkSelector: "[role=action-title]"
            }
        },
        {
            selector: '[data-ng-click="reset()"]',
            action: "reset",
            value: {
                checkSelector: 'ng-pluralize'
            }

        },
        {
            selector: '[data-ng-click="search()"]',
            action: "search",
            value: {
                checkSelector: 'ng-pluralize',
                checkUrl: /search$/
            }
        },

        // Individual Drop Down and Text Input Test
        {
            selector: '[data-type="Individual"]',
            action: "click"
        },
        {
            selector: '[data-ng-model="searchCriteria.provider_last_name_legal_name"]',
            action: "sendKeys",
            value: {
                textToEnter: "jones"
            }

        },
        {
            selector: '[data-ng-click="search()"]',
            action: "search",
            value: {
                checkSelector: 'ng-pluralize',
                checkUrl: /provider_last_name_legal_name/
            }
        },
        {
            action: 'screenshot',
            value: {
                checkUrl: /provider_last_name_legal_name/,
                fileName: '3-mainToggleLast',
                checkSelector: "[role=action-title]"
            }
        },
        {
            selector: '[data-ng-click="reset()"]',
            action: "reset",
            value: {
                checkSelector: 'ng-pluralize'
            }

        },
        {
            selector: '[data-ng-click="search()"]',
            action: "search",
            value: {
                checkSelector: 'ng-pluralize',
                checkUrl: /search$/
            }

        },
        {
            selector: '[data-ng-model="searchCriteria.provider_first_name"]',
            action: "sendKeys",
            value: {
                textToEnter: "jones"
            }
        },
        {
            selector: '[data-ng-click="search()"]',
            action: "search",
            value: {
                checkSelector: 'ng-pluralize',
                checkUrl: /search$/
            }
        },
        {
            action: 'screenshot',
            value: {
                checkUrl: /provider_first_name/,
                fileName: '4-mainToggleFirst',
                checkSelector: "[role=action-title]"
            }

        },
        {
            selector: '[data-ng-click="reset()"]',
            action: "reset",
            value: {
                checkSelector: 'ng-pluralize'
            }
        },
        {
            selector: '[data-ng-click="search()"]',
            action: "search",
            value: {
                checkSelector: 'ng-pluralize',
                checkUrl: /search$/
            }
        },
        {
            selector: '[data-type="Individual"]',
            action: "click"

        },

        //Organization Drop Down and Text Input Test
        {
            selector: '[data-type="Organization"]',
            action: "click"
        },
        {
            selector: '[data-ng-model="searchCriteria.provider_organization_name_legal_business_name"]',
            action: "sendKeys",
            value: {
                textToEnter: 'smi'
            }

        },
        {
            selector: '[data-ng-click="search()"]',
            action: "search",
            value: {
                checkSelector: 'ng-pluralize',
                checkUrl: /provider_organization_name_legal_business_name/
            }
        },

        {
            action: 'screenshot',
            value: {
                checkUrl: /search$/,
                fileName: '5-searchOrganization',
                checkSelector: "[role=action-title]"
            }
        },
        {
            selector: '[data-ng-click="reset()"]',
            action: "reset",
            value: {
                checkSelector: 'ng-pluralize'
            }
        },
        {
            selector: '[data-ng-click="search()"]',
            action: "search",
            value: {
                checkSelector: 'ng-pluralize',
                checkUrl: /search$/
            }
        },
        {
            selector: '[data-type="Organization"]',
            action: "click"
        },

        //Affiliations Drop Down and Text Input Test

        {
           selector: '[data-type="Affiliations"]',
            action: "click"
        },
        {
            selector: '[data-ng-model="searchCriteria.affiliations_org_from"]',
            action: "sendKeys",
            value: {
                textToEnter: '1'
            }

        },
        {
            selector: '[data-ng-model="searchCriteria.affiliations_org_to"]',
            action: "sendKeys",
            value: {
                textToEnter: '3'
            }

        },
        {
            selector: '[data-ng-click="search()"]',
            action: "search",
            value: {
                checkSelector: 'ng-pluralize',
                checkUrl: /search\?affiliations_org_from/
            }
        },
        {
            action: 'screenshot',
            value: {
                checkUrl: /search$/,
                fileName: '6-searchAffiliations',
                checkSelector: "[role=action-title]"
            }
        },
        {
            selector: '[data-ng-click="reset()"]',
            action: "reset",
            value: {
                checkSelector: 'ng-pluralize'
            }
        },
        {
            selector: '[data-ng-click="search()"]',
            action: "search",
            value: {
                checkSelector: 'ng-pluralize',
                checkUrl: /search$/
            }
        },
        {
            selector: '[data-type="Affiliations"]',
            action: "click"
        },

        // Specialty Drop Down and Text Input Test

        {
           selector: '[data-type="Specialty"]',
            action: "click"
        },
        {
            selector: '[data-ng-model="instantSearchCriteria"]',
            action: "sendKeys",
            value: {
                textToEnter: 'gastro'
            }

        },
        {
            selector: '[data-ng-click="updateList()"]',
            action: "click"
        },
        {
            selector: '[data-ng-click="search()"]',
            action: "search",
            value: {
                checkSelector: 'ng-pluralize',
                checkUrl: /search\?taxonomies/
            }
        },
        {
            action: 'screenshot',
            value: {
                checkUrl: /search$/,
                fileName: '7-searchSpecialty',
                checkSelector: "[role=action-title]"
            }
        },
        {
            selector: '[data-ng-click="reset()"]',
            action: "reset",
            value: {
                checkSelector: 'ng-pluralize'
            }
        },
        {
            selector: '[data-ng-click="search()"]',
            action: "search",
            value: {
                checkSelector: 'ng-pluralize',
                checkUrl: /search$/
            }
        },
        {
            selector: '[data-type="Specialty"]',
            action: "click"
        }



    ];

    var actions = {
        sendKeys: function (selector, val) {
            casper.waitForSelector(selector,
                function success() {
                    test.assertExists(selector);
                    this.sendKeys(selector, val.textToEnter);
                },
                function fail() {
                    test.assertExists(selector);
                }
            );
        },
        click: function (selector) {
            casper.waitForSelector(selector,
                function success() {
                    test.assertExists(selector);
                    console.log("Clicking the ", selector, " button")
                    this.mouse.click(selector);
                },
                function fail() {
                    test.assertExists(selector);
                }
            );
        },

        screenshot: function (selector, opts) {
            casper.waitForUrl(opts.checkUrl, function () {}, function () {}, 10000);

            casper.waitForSelector(opts.checkSelector,
                function success() {
                    console.log('click ok, new location is ' + this.getCurrentUrl());
                    console.log("Making a screenshot and save it as .png");
                    this.capture(opts.fileName + '.png');
                }
            );
        },


        //loop that will add "a" to each field that takes an alpha key
        // Input the letter "a" into the field
        letterInputLast: function (selector, value) {
            casper.waitForSelector(selector,
                function success() {
                    //test.assertExists(selector);
                    this.sendKeys(selector,value);
                });
        },

        search: function (selector, value) {
            casper.waitForSelector(selector,
                function success() {
                    //test.assertExists(selector);
                    console.log("Clicking the ", selector, " button");
                },

                function fail() {
                    test.assertExists(selector);
                }
            );
            casper.then(function () {
                this.click(selector);
            });
            casper.waitForUrl(value.checkUrl, function () {
                this.echo(this.fetchText(value.checkSelector));
            }, function () {}, 10000);
        },


        reset: function (selector) {
            casper.waitForSelector(selector,
                function success(a) {
                    //test.assertExists(selector);
                    //console.log("Clicking the ", selector, " button");
                    this.mouse.click(selector);
                    //call search function
                },

                function fail() {
                    test.assertExists(selector);
                }
            );
        },



        run: function () {
            casper.run(function () {
            });
        }
    };

    casper.start('http://192.168.1.105:5001/login');

    loginTester.forEach(function (testStep) {
        actions[testStep.action](testStep.selector, testStep.value);
    });

    casper.run(function () {
        test.done();
    });


});
  


  