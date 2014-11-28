var AngularRemote;
(function (AngularRemote) {
    var Patcher = new AngularRemote.PatchProcessor();
    function EvalToProxy(str) {
        var obj = eval("(" + str + ")");
        AngularRemote.JsonPointer.AttachPointers(obj);
        return obj;
    }
    AngularRemote.EvalToProxy = EvalToProxy;
    function LogIncomming(str) {
        var e = document.getElementById("Incomming");
        if(e) {
            e.innerHTML = e.innerHTML + "\r\n" + str;
        }
    }
    AngularRemote.LogIncomming = LogIncomming;
    function LogOutgoing(str) {
        var e = document.getElementById("Outgoing");
        if(e) {
            e.innerHTML = e.innerHTML + "\r\n" + str;
        }
    }
    AngularRemote.LogOutgoing = LogOutgoing;
    function Patch(patches, viewmodel) {
        var cnt = patches.length;
        for(var t = 0; t < cnt; t++) {
            var p = patches[t];
            Patcher[p.op](p, viewmodel);
        }
    }
    AngularRemote.Patch = Patch;
    function CopyProperties(from, to) {
        for(var key in from) {
            to[key] = from[key];
        }
    }
    AngularRemote.CopyProperties = CopyProperties;
    ; ;
    function Bootstrap() {
        angular.module('AngularRemote', []).directive('appMockup', function () {
            return {
                restrict: 'A',
                link: function (scope, elem, attr) {
                    scope.__AppMockup = attr.appMockup;
                }
            };
        }).directive('appMockupPatch', function () {
            return {
                restrict: 'A',
                link: function (scope, elem, attr) {
                    scope.__AppMockupPatch = attr.appMockupPatch;
                }
            };
        }).directive('app', function () {
            return {
                restrict: 'A',
                link: function (scope, element, attrs) {
                    if(!this.func) {
                        this.func = eval("(function( scope, element, attrs ) { if ( scope." + attrs.app + " != undefined ) element.html( scope." + attrs.app + ".__vc  ); else element.html(\"No content in " + attrs.app + "\"); })");
                    }
                    console.log(this.func);
                    return this.func.call(null, scope, element, attrs);
                }
            };
        }).directive('app2', function () {
            return {
                restrict: 'ECA',
                terminal: true,
                compile: function (element, attr) {
                    var srcExp = attr.app2;
                    var autoScrollExp = attr.autoscroll;

                    return function (scope, element) {
                        var changeCounter = 0;
                        var childScope;

                        var $compile = (window).JockeTemp;
                        var clearContent = function () {
                            if(childScope) {
                                childScope.$destroy();
                                childScope = null;
                            }
                            element.html('');
                        };
                        if(srcExp) {
                            if(childScope) {
                                childScope.$destroy();
                            }
                            childScope = scope.$new();
                            element.html("<ul><li>{{Test}}</li></ul>");
                            $compile(element.contents())(childScope);
                            childScope.$emit('$includeContentLoaded');
                        } else {
                            clearContent();
                        }
                    }
                }
            };
        }).provider('$parse', function () {
            var cache = {
            };
            ((this.$get)) = [
                '$filter', 
                '$sniffer', 
                function ($filter, $sniffer) {
                    return function (exp) {
                        switch(typeof exp) {
                            case 'string': {
                                return cache.hasOwnProperty(exp) ? cache[exp] : cache[exp] = AngularRemote.parser2(exp, false, $filter, $sniffer.csp);

                            }
                            case 'function': {
                                return exp;

                            }
                            default: {
                                return angular.noop;

                            }
                        }
                    }
                }            ];
        });
        angular.element(document).ready(function () {
            AngularRemote.Bootstrap();
            var injector = angular.injector([
                "ng", 
                "AngularRemote"
            ]);
            var rootScope = injector.get('$rootScope');
            var compile = injector.get('$compile');
            (window).JockeTemp = compile;
            var doc = angular.element(document);
            var q = injector.get("$q");
            doc.data('$injector', injector);
            rootScope.$apply(function () {
                compile(doc)(rootScope);
            });
            if(true) {
                var xhrobj = new XMLHttpRequest();
                xhrobj.open('GET', rootScope.__AppMockup);
                xhrobj.onreadystatechange = function () {
                    if(xhrobj.readyState == 4) {
                        if(xhrobj.status == 200) {
                            var appJs = xhrobj.responseText;
                            var js = AngularRemote.EvalToProxy(appJs);
                            AngularRemote.CopyProperties(js, rootScope);
                            rootScope.$digest();
                            xhrobj = new XMLHttpRequest();
                            xhrobj.open('GET', rootScope.__AppMockupPatch);
                            xhrobj.onreadystatechange = function () {
                                if(xhrobj.readyState == 4) {
                                    if(xhrobj.status == 200) {
                                        var appJs = xhrobj.responseText;
                                        LogIncomming(appJs);
                                        var x = eval("(" + appJs + ")");
                                        AngularRemote.Patch(x, rootScope);
                                        rootScope.$digest();
                                    }
                                }
                            };
                            xhrobj.send(null);
                        }
                    }
                };
                xhrobj.send(null);
            } else {
                console.log("veem=" + JSON.stringify(__elim_req));
                var js = __elim_req;
                AngularRemote.CopyProperties(js, rootScope);
                rootScope.$apply();
            }
        });
    }
    AngularRemote.Bootstrap = Bootstrap;
})(AngularRemote || (AngularRemote = {}));

AngularRemote.Bootstrap();
