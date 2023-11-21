from pyswip import Prolog

prl = Prolog()
prl.consult('newKB.pl')
#prl.consult("knowledgeBase.pl")

def pickOne(languages, area):
    #Agenda for picking the best language
    orderByArea = {'frontend_web_development': ['javascript', 'rust', 'go', 'cs', 'r'],
                   'backend_web_development' : ['javascript', 'python', 'ruby', 'php', 'cs', 'swift', 'go', 'rust', 'perl', 'r'],
                   'data_science' : ['python', 'r', 'julia', 'matlab', 'javascript', 'java', 'cpp', 'swift', 'c', 'go'],
                   'desktop_development' : ['java', 'cpp', 'cs', 'kotlin', 'swift', 'python','javascript', 'ruby', 'php', 'go'],
                   'mobile_development' : ['swift', 'java', 'kotlin', 'dart', 'cs', 'go', 'ruby'],
                   'game_development' : ['cpp', 'cs', 'java', 'python', 'javascript', 'lua'],
                   'general_purpose' : ['python', 'javascript', 'java', 'cs', 'cpp', 'c', 'go']}
    orderLanguages = sorted(languages, key=lambda x: orderByArea[area].index(x))
    return orderLanguages[0]

def definition(language):
    definitions = {
        'python' : """ Python is a high-level, interpreted, and general-purpose programming language known for its simplicity and readability. It emphasizes code readability and provides a large standard library, making it suitable for a wide range of applications, including web development, data analysis, machine learning, and automation.""", 
        'javascript' : """JavaScript is a versatile, interpreted programming language primarily used for web development. It enables dynamic behavior and interactivity in web pages. JavaScript can also be used on the server-side (Node.js) and for building cross-platform mobile applications (React Native).""",
        'ruby' : """Ruby is a dynamic, object-oriented programming language known for its elegant syntax and focus on simplicity. It prioritizes developer happiness and emphasizes readability and productivity. Ruby is commonly used for web development with the Ruby on Rails framework.""",
        'swift' : """Swift is a modern, compiled programming language developed by Apple for iOS, macOS, watchOS, and tvOS app development. It is designed to be safe, fast, and expressive, with a syntax that aims for simplicity and clarity.""",
        'php' : """PHP is a server-side, interpreted scripting language widely used for web development. It is primarily used for building dynamic websites and web applications. PHP offers extensive database connectivity options and works well with HTML to create dynamic web content.""",
        'cs' : """C# (C Sharp) is a general-purpose, object-oriented programming language developed by Microsoft. It is part of the .NET framework and is commonly used for building Windows applications, web development with ASP.NET, and game development with Unity.""",
        'go' : """Go, also known as Golang, is a statically typed, compiled language developed by Google. It aims to provide simplicity, efficiency, and built-in concurrency support. Go is known for its performance and is commonly used for network programming, web servers, and distributed systems.""",
        'perl' : """Perl is a highly capable, interpreted programming language known for its strong text processing capabilities. It is often used for system administration, web development, and network programming. Perl prioritizes flexibility and allows for various programming paradigms.""",
        'r' : """R is a statistical programming language used for data analysis, visualization, and statistical modeling. It provides a wide range of statistical and graphical techniques and has a vibrant ecosystem of packages specifically designed for data science and statistical analysis.""",
        'julia' : """Julia is a high-level, dynamic programming language designed for numerical and scientific computing. It combines the ease of use of high-level languages with the performance of low-level languages. Julia is popular among data scientists and researchers working in fields like machine learning, optimization, and data analysis.""",
        'matlab' : """MATLAB is a proprietary programming language and environment for numerical computing and scientific visualization. It is widely used in academia and industry for tasks such as data analysis, simulation, and algorithm development. MATLAB provides extensive mathematical functions and toolboxes for various domains.""", 
        'java' : """Java is a popular, general-purpose, and object-oriented programming language known for its platform independence. It is widely used for developing enterprise-level applications, Android apps, web applications, and large-scale systems. Java emphasizes write once, run anywhere (WORA) with its "write once, run anywhere" philosophy.""",
        'c' : """C is a low-level, general-purpose programming language known for its efficiency and direct control over hardware resources. It is widely used in system programming, embedded systems, and developing operating systems. C is considered the foundation for many other programming languages.""",
        'rust' : """Rust is a systems programming language focused on safety, concurrency, and performance. It aims to provide memory safety, without sacrificing performance, through its ownership and borrowing system. Rust is used for low-level system programming, building high-performance applications, and developing safe and concurrent software.""",
        'scala' : """Scala is a statically typed, object-oriented, and functional programming language that runs on the Java Virtual Machine (JVM). It combines object-oriented and functional programming paradigms and provides powerful features for building scalable and concurrent applications.""",
        'cpp' : """C++ is a general-purpose, high-level programming language known for its efficiency and control over hardware resources. It extends the C language with features like object-oriented programming, templates, and standard libraries. C++ is commonly used for system programming, game development, and performance-critical applications.""",
        'kotlin' : """Kotlin is a modern, statically typed programming language developed by JetBrains. It is designed to be fully interoperable with Java and runs on the Java Virtual Machine (JVM). Kotlin offers concise syntax, null safety, and support for functional programming. It is commonly used for Android app development and server-side applications.""",
        'dart' : """Dart is a client-optimized, open-source programming language developed by Google. It is used for building web and mobile applications, primarily through the Flutter framework. Dart offers a combination of AOT (Ahead of Time) and JIT (Just in Time) compilation, providing high-performance and productivity.""",
        'lua' : """ Lua is a lightweight, high-level scripting language designed for embedded systems and extensibility. It is often used as a scripting language within larger applications and game engines. Lua is known for its simplicity, flexibility, and ease of integration into existing projects."""}
    return definitions[language]



    
