% Languages facts
language(python).
language(javascript).
language(ruby).
language(swift).
language(php).
language(cs).
language(go).
language(perl).
language(r).
language(julia).
language(matlab).
language(java).
language(c).
language(rust).
language(scala).
language(cpp).
language(kotlin).
language(dart).
language(lua).

% Frameworks facts
framework(javascript, reactjs, frontend_web_development).
framework(javascript, reactnative, frontend_web_development).
framework(javascript, angularjs, frontend_web_development).
framework(javascript, vuejs, frontend_web_development).
framework(javascript, restify, backend_web_development).
framework(javascript, nodejs, backend_web_development).
framework(javascript, emberjs, frontend_web_development).
framework(python, django, backend_web_development).
framework(python, flask, backend_web_development).
framework(python, cherrypy, backend_web_development).
framework(python, pyramid, backend_web_development).
framework(python, bottle, backend_web_development).
framework(ruby, rubyonrails, backend_web_development).
framework(ruby, sinatra, backend_web_development).
framework(ruby, ramaze, backend_web_development).
framework(swift, vapor, backend_web_development).
framework(swift, kitura, backend_web_development).
framework(swift, swiftnio, backend_web_development).
framework(php, laravel, backend_web_development).
framework(php, symfony, backend_web_development).
framework(php, codeigniter, backend_web_development).
framework(php, phalcon, backend_web_development).
framework(php, cakephp, backend_web_development).
framework(cs, aspdotnet, frontend_web_development).
framework(cs, aspdotnet, backend_web_development).
framework(rust, actixweb, backend_web_development).
framework(rust, rocket, backend_web_development).
framework(rust, axum, backend_web_development).
framework(rust, gotham, backend_web_development).
framework(rust, tide, backend_web_development).
framework(rust, tauri, frontend_web_development).
framework(go, fasthttp, frontend_web_development).
framework(go, fasthttp, backend_web_development).
framework(go, gin, backend_web_development).
framework(go, beego, backend_web_development).
framework(go, iris, backend_web_development).
framework(go, fiber, backend_web_development).
framework(perl, catalyst, backend_web_development).
framework(perl, dancer, backend_web_development).
framework(perl, mojolicious, backend_web_development).
framework(perl, maypole, backend_web_development).
framework(r, shiny, frontend_web_development).
framework(r, fiery, frontend_web_development).
framework(r, plumber, backend_web_development).

% Features:

% Features about area
feature(frontend_web_development, [javascript, cs, rust, go, r]).
feature(backend_web_development, [javascript, python, ruby, swift, php, cs, rust, go, perl, r]).
feature(data_science, [python, r, julia, go, matlab, javascript, java, c, cpp, swift]).
feature(desktop_development, [java, javascript, cs, kotlin, python, ruby, php, cpp, go, swift]).
feature(mobile_development, [swift, java, kotlin, dart, ruby, go, cs]).
feature(game_development, [cs, cpp, java, javascript, python, lua]).
feature(general_purpose, [python, c, javascript, java, cs, cpp, go]).

% Other features 
feature(easy_to_use, [python, javascript, ruby, php, kotlin, lua, dart]).
feature(big_community, [python, javascript, java, c, cpp, cs, go, swift, php]).
feature(open_source, [python, javascript, java, c, cpp, r, julia, scala, go, ruby, php, rust, perl, lua]).
feature(high_performance, [java, c, cpp, cs, go, swift, rust]).
feature(high_security, [java, cpp, cs, julia, swift, ruby, rust, kotlin]).
feature(beginner_level, [python, javascript, ruby, php, perl, lua]).
feature(intermediate_level, [java, c, cpp, r, swift, kotlin, dart, python, javascript, ruby, php, perl, lua]).
feature(expert_level, [cs, julia, scala, go, matlab, rust, java, c, cpp, r, swift, kotlin, dart, python, javascript, ruby, php, perl, lua]).
feature(easy_to_maintain, [python, ruby, swift, go, julia, kotlin, dart, lua]).
feature(compiled, [c, cpp, rust, swift, go, java, kotlin, dart, scala, cs, julia]).
feature(interpreted, [python, javascript, ruby, php, perl, r, matlab, lua]).

% Rule for finding the languages satisfying the choosen features
recommendLanguage([Feature | Rest], Language) :- feature(Feature, Languages), member(Language, Languages), recommendLanguage(Rest, Language).
recommendLanguage([], _).


% Rule for recommending frameworks
recommendFramework(Framework, Language, Feature) :- framework(Language, Framework, Feature).
