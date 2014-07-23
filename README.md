Sentry plugin for [B3](http://www.bigbrotherbot.net/ "BigBrotherBot")
=====================================================================

Installation
------------
1. Copy the file [extplugins/sentry.py](extplugins/sentry.py) into your `b3/extplugins` folder and
[extplugins/conf/plugin_sentry.ini](extplugins/conf/plugin_sentry.ini) into your `b3/conf` folder
2. This plugin requires the [raven-python](http://raven.readthedocs.org/en/latest/install/index.html#install) module.
3. Add the following line in your b3.xml file (below the other plugin lines)
```xml
<plugin name="sentry" config="@conf/plugin_sentry.ini"/>
```

