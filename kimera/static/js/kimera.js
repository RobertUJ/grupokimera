var Kimera = {
	init:function(){
		this.menu();
	},
	menu: function(){
		var menuLeft = document.getElementById( 'cbp-spmenu-s1' ),
		    showLeft = document.getElementById( 'menu-main' ),
		    body = document.body;
 
		showLeft.onclick = function(e) {
			e.preventDefault();
			var btn = $("this");
			btn.toggleClass('active');
			$(menuLeft).toggleClass("cbp-spmenu-open");
		};
		
	}
}

Kimera.init();