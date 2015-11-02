var mappings = {
	"var1": function(c) {console.log(c + "1"); },
	"var2": function(c) {console.log("1" + c); }
};

[
	{selector:"var1", value: "ello"},
	{selector:"var1", value: "llo"},
	{selector:"var2", value: "elo"},
	{selector:"var1", value: "eo"},
	{selector:"var2", value: "e"}
	].forEach(function(selector){
		mappings[selector.selector](selector.value);
	});