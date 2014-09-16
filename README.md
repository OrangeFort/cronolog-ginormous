<img src='https://secure.orangefort.com/images/orange_fort.png' />

[Cronolog](http://cronolog.org/) was once used to split and rotate log streams from long-running server processes, because we didn't have [Logstash](http://logstash.net/). This repo contains a RPM spec file for RHEL/CentOS 7, and a gigantic patch. The patch adds numerous features to Cronolog, like:

* setting a UMASK on logfiles
* specifying UID and GID on logfiles
* calling a helper script after log rotation
* compiling on a modern platform

### Caveat Lector
While my work (the spec file) is APL 2.0, the ginormous patch is a synthesis of many other smaller patches which may feature different licenses. I'm in the process of tracking down all of the disperate patches and making sure that their license terms are clear.
