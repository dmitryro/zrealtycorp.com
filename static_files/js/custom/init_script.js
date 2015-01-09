$(function(){
                                function format(item) { return item.tag; }
                             //   $("#id_subject").select2({);

        //                        $('#contact-form').pep(); 
     
                                $('#contact-close').bind('click',function(){
                                        $('#contact-form').css('display','none');
                                });
                                $('#contact-form').css('display','none'); 
                                $(".group1").colorbox({rel:'group1'});
                                $(".ajax").colorbox();
                                $(".youtube").colorbox({iframe:true, innerWidth:640, innerHeight:390});
                                $(".vimeo").colorbox({iframe:true, innerWidth:500, innerHeight:409});
                                $(".iframe").colorbox({iframe:true, width:"80%", height:"80%"});
                                $(".inline").colorbox({inline:true, width:"50%"});
                                $(".callbacks").colorbox({
                                        onOpen:function(){ alert('onOpen: colorbox is about to open'); },
                                        onLoad:function(){ alert('onLoad: colorbox has started to load the targeted content'); },
                                        onComplete:function(){ alert('onComplete: colorbox has displayed the loaded content'); },
                                        onCleanup:function(){ alert('onCleanup: colorbox has begun the close process'); },
                                        onClosed:function(){ alert('onClosed: colorbox has completely closed'); }
                                });

                                $('.non-retina').colorbox({rel:'group5', transition:'none'})
                                $('.retina').colorbox({rel:'group5', transition:'none', retinaImage:true, retinaUrl:true});



             $("#search a").on( "click", function() {
                                        
                                             $('#properties-area').css('display','none');
                                             open = $("#is_search_open").val();
                                             if (open==undefined || !open) {
                                                 $("#is_search_open").attr('value','true');
                                             }
                                             if (open=='false') {
                                                 $("#is_search_open").attr('value','true');
                                                 $("#search-area").css('display','block');
                                            //     $("#search_area").css('height','80px');
                                            //     $("#container").css('margin-top','180px');


                                                 $('#submenu-wrapper-1').css('margin-top','-8.85em');
                                                 $('#submenu-wrapper-2').css('margin-top','-8.85em');
                                                 $('#submenu-wrapper-3').css('margin-top','-8.85em');
                                              }
                                             if (open=='true'){
                                                 $("#is_search_open").attr('value','false');
                                                 $("#search-area").css('display','none');
                                                 $('#submenu-wrapper-1').css('margin-top','-2.5em');
                                                 $('#submenu-wrapper-2').css('margin-top','-2.5em');
                                                 $('#submenu-wrapper-3').css('margin-top','-2.5em');
 
                                             }

                                       /// alert(open);
                                             return false;
                                         }
              );
               $("#bnt_search").on("click",function() {
                     $("#homepage_list").html('');
                      $("#homepage_list").css('display','none');
                      $("#search_header").css('display','block');
               });


               $("#home a").on( "click", function() {
                                 var ref = window.location.href;
                                 prop_open = $("#is_properties_open").val();
                                 if  (ref.indexOf('property')!= -1) {
                                      $("#container").attr("src",'http://zrealtycorp.com');
				      window.location.href = "http://zrealtycorp.com";
									        
				 }
		                 if  (ref=='http://zrealtycorp.com/contact/') {
                                      $("#container").attr("src",'http://zrealtycorp.com');
                                      window.location.href = "http://zrealtycorp.com";
                                 }
                                 if  (ref=='http://zrealtycorp.com/blog/') {
                                      $("#container").attr("src",'http://zrealtycorp.com');
                                      window.location.href = "http://zrealtycorp.com";
                                 }
                                 if(ref=='http://zrealtycorp.com/contact/') {
                                      $("#container").attr("src",'http://zrealtycorp.com');
                                      window.location.href = "http://zrealtycorp.com";
                                 }
                                 $("#search-area").css('display','none');
                                 if (prop_open==undefined || !prop_open) {
                                     $("#is_properties_open").attr('value','true');
                                 }
                                 if (prop_open=='false') {
                                     $("#is_properties_open").attr('value','true');
                                     $("#properties-area").css('display','block');
                                 }
                                 if (prop_open=='true'){
                                     $("#is_properties_open").attr('value','false');
                                     $("#properties-area").css('display','none');
				 }
                                 return false;
              });
              $('#search a').qtip({ // Grab some elements to apply the tooltip to
                     content: {
                           text: 'Search the properties'
                     },
                     style: {
                           classes: 'qtip-default  qtip qtip-tipped'
                     },
                     position: {
                           target: $('#search_tooltip')
                     }
               });
              $('#contact a').qtip({ // Grab some elements to apply the tooltip to
                     content: {
                           text: 'Contact us'
                     },
                     style: {
                           classes: 'qtip-default  qtip qtip-tipped'
                     },
                     position: {
                           target: $('#contact_tooltip')
                     }

               });


              $('#social_1 a').qtip({ // Grab some elements to apply the tooltip to
                     content: {
                           text: '<span style="font-size:12px;"><a href="#">Follow us on Facebook</a></span>'
                     },
                     style: {
                           classes: 'qtip-default  qtip qtip-tipped',
                           tip: {
                               corner: 'right top',
                               mimic: 'right center'
                           }
                     },
                     position: {
                           target: $('#social_1_tooltip')
                     }
              });


              $('#social_2 a').qtip({ // Grab some elements to apply the tooltip to
                     content: {
                           text: '<span style="font-size:12px;"><a href="#">Follow us on LinkedIn</a></span>'
                     },
                     style: {
                           classes: 'qtip-default  qtip qtip-tipped',
                           tip: {
                               corner: 'right top',
                               mimic: 'right center'
                           }
                     },
                     position: {
                           target: $('#social_2_tooltip')
                     }
              });

              $('#social_3 a').qtip({ // Grab some elements to apply the tooltip to
                     content: {
                           text: '<span style="font-size:12px;"><a href="#">Follow us on Twitter</a></span>'
                     },
                     style: {
                           classes: 'qtip-default  qtip qtip-tipped',
                           tip: {
                               corner: 'right top',
                               mimic: 'right center'
                           }
                     },
                     position: {
                           target: $('#social_3_tooltip')
                     }
              });
              $('#social_4 a').qtip({ // Grab some elements to apply the tooltip to
                     content: {
                           text: '<span style="font-size:12px;"><a href="#">Follow us on YouTube</a></span>'
                     },
                     style: {
                           classes: 'qtip-default  qtip qtip-tipped',
                           tip: {
                               corner: 'right top',
                               mimic: 'right center'
                           }
                     },
                     position: {
                           target: $('#social_4_tooltip')
                     }
              });
              $('#social_5 a').qtip({ // Grab some elements to apply the tooltip to
                     content: {
                           text: '<span style="font-size:12px;"><a href="#">Follow us on Google Plus</a></span>'
                     },
                     style: {
                           classes: 'qtip-default  qtip qtip-tipped',
                           tip: {
                               corner: 'right top',
                               mimic: 'right center'
                           }
                     },
                     position: {
                           target: $('#social_5_tooltip')
                     }
              });
              $('#social_6 a').qtip({ // Grab some elements to apply the tooltip to
                     content: {
                           text: '<span style="font-size:12px;"><a href="#">Read our RSS Feed</a></span>'
                     },
                     style: {
                           classes: 'qtip-default  qtip qtip-tipped',
                           tip: {
                               corner: 'right top',
                               mimic: 'right center'
                           }
                     },
                     position: {
                           target: $('#social_6_tooltip')
                     }
              });
              $('#back_btn a').qtip({ // Grab some elements to apply the tooltip to
                     content: {
                           text: '<span style="font-size:12px;"><a href="#">Back to the list</a></span>'
                     },
                     style: {
                           classes: 'qtip-default  qtip qtip-tipped',
                           tip: {
                               corner: 'right top',
                               mimic: 'right center'
                           }
                     },
                     position: {
                           target: $('#back_btn_tooltip')
                     }
              });
 
      });

