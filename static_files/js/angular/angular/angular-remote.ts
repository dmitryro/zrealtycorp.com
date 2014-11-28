
///<reference path="Parser.ts" />
///<reference path="../object-observe/proxy.ts" />
///<reference path="../json-patch/patch-processor.ts"/>

declare var angular;
declare var __elim_req: string;

module AngularRemote {

    var Patcher = new PatchProcessor();

    export function EvalToProxy(str: string) {
//        return Wrap(eval("(" + str + ")"));
        var obj = eval("(" + str + ")");
        JsonPointer.AttachPointers(obj);
        return obj;
//        return eval("(" + str + ")");
    }

    export function LogIncomming( str: string) {
        var e = document.getElementById("Incomming");
        if (e)
            e.innerHTML = e.innerHTML + "\r\n" + str;
    }

    export function LogOutgoing( str: string) {
        var e = document.getElementById("Outgoing");
        if (e)
            e.innerHTML = e.innerHTML + "\r\n" + str;
    }

    // Applies a Json Patch (http://tools.ietf.org/html/draft-ietf-appsawg-json-patch-05)
    // array supplied in 'patches' to the view-model supplied in 'viewmodel'
    export function Patch(patches: any[], viewmodel:any) {
        var cnt = patches.length;
        for (var t = 0 ; t < cnt ; t++ ) {
            var p = patches[t];
            Patcher[p.op](p,viewmodel);
        }
    }

    export function CopyProperties(from: Object, to: Object) {
        for (var key in from) {
            //   if (from.hasOwnProperty(key)) {
            to[key] = from[key];
            //   }
        }
    };

    export function Bootstrap() {

        angular.module('AngularRemote', [])
            .directive('appMockup', function () {
                return {
                    restrict: 'A',
                    link:
                        function (scope, elem, attr) {
                            scope.__AppMockup = attr.appMockup;
                        }
                }
            })
            .directive('appMockupPatch', function () {
                return {
                    restrict: 'A',
                    link:
                        function (scope, elem, attr) {
                            scope.__AppMockupPatch = attr.appMockupPatch;
                        }
                }
            })
            .directive('app', function () {
                return {
                    restrict: 'A',
                    link: function (scope, element, attrs) {
                        if (!this.func) {
                            this.func = eval("(function( scope, element, attrs ) { if ( scope." + attrs.app + " != undefined ) element.html( scope." +
                                        attrs.app +
                                        ".__vc  ); else element.html(\"No content in " + attrs.app + "\"); })")
                        }
                        console.log(this.func);
                        return this.func.call(null, scope, element, attrs);
                    }
                }
            }).

            directive('app2', function () {

                return {
                    restrict: 'ECA',
                    terminal: true,
                    compile: function (element, attr ) {
                      var srcExp = attr.app2,
                          autoScrollExp = attr.autoscroll;

                        return function (scope, element) {
                          var changeCounter = 0,
                              childScope;

                            //var $compile = Starcounter.AngularInjector.get('$compile');
                          var $compile = (<any>window).JockeTemp;

                            var clearContent = function () {
                                if (childScope) {
                                    childScope.$destroy();
                                    childScope = null;
                                }

                                element.html('');
                            };

                            //scope.$watch(srcExp, function(src) {
                            //  var thisChangeId = ++changeCounter;

                            if (srcExp) {
                                //            $http.get(src, {cache: $templateCache}).success(function(response) {
                                //      if (thisChangeId !== changeCounter) return;

                                if (childScope) childScope.$destroy();
                                childScope = scope.$new();

                                element.html("<ul><li>{{Test}}</li></ul>");
                                //if (scope.Page != undefined)
                                //    console.log( "Found " + scope.Page.__vc);
                                $compile(element.contents())(childScope);

                                // if (isDefined(autoScrollExp) && (!autoScrollExp || scope.$eval(autoScrollExp))) {
                                //   $anchorScroll();
                                         // }

                                childScope.$emit('$includeContentLoaded');
                                //              scope.$eval(onloadExp);
                            }
                            else clearContent();
                            //});
                        };
                    }
                };
            })
            .provider('$parse', function () {
                var cache = {};

                (<any[]>(this.$get)) = ['$filter', '$sniffer', function ($filter, $sniffer) {
                    return function (exp) {
                        switch (typeof exp) {
                            case 'string':
                                return cache.hasOwnProperty(exp)
                                  ? cache[exp]
                                  : cache[exp] = parser2(exp, false, $filter, $sniffer.csp);
                            case 'function':
                                return exp;
                            default:
                                return angular.noop;
                        }
                    };
                }];
            });

        angular.element(document).ready(function () {
            AngularRemote.Bootstrap();
            var injector = angular.injector(["ng", "AngularRemote"]);
            var rootScope = injector.get('$rootScope');
            var compile = injector.get('$compile');
            (<any>window).JockeTemp = compile;
            var doc = angular.element(document);


            var q = injector.get("$q");
            doc.data('$injector', injector);
            rootScope.$apply(function () { compile(doc)(rootScope); });

            if (true) { //__elim_req == null) {     
                var xhrobj = new XMLHttpRequest();
                xhrobj.open('GET', rootScope.__AppMockup);

                xhrobj.onreadystatechange = function () {
                    if (xhrobj.readyState == 4) {
                        if (xhrobj.status == 200) {
                            var appJs = xhrobj.responseText;
                            //LogIncomming(appJs);
                            var js = AngularRemote.EvalToProxy(appJs);
                            AngularRemote.CopyProperties(js, rootScope);
                            rootScope.$digest();
                            // ----- 

                            xhrobj = new XMLHttpRequest();
                            xhrobj.open('GET', rootScope.__AppMockupPatch);

                            xhrobj.onreadystatechange = function () {
                                if (xhrobj.readyState == 4) {
                                    if (xhrobj.status == 200) {
                                        var appJs = xhrobj.responseText;
                                        LogIncomming(appJs);
                                        var x: any[] = eval("(" + appJs + ")");
                                        AngularRemote.Patch(x, rootScope);
                                        rootScope.$digest();
                                    }
                                }
                            }

                            xhrobj.send(null);
                        }
                    }



                }

                xhrobj.send(null);


            }
            else {

                //                vm = b64_to_utf8(vm);
                //                delete_cookie("vm");
                console.log("veem=" + JSON.stringify(__elim_req));

                var js = __elim_req; //Starcounter.sample(vm);
                AngularRemote.CopyProperties(js, rootScope);
                rootScope.$apply();


            }
        });

    }
}

AngularRemote.Bootstrap();