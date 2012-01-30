gevent-viz
==========

gevent-viz is a friendly fork of [eventlet_visualiser](https://github.com/colinhowe/eventlet_visualiser)

It monkey patches the Greenlet module to trace the execution of all Greenlets and stores the data in flat file. You can visualize the resulting profile in HTML.

Originally released for eventlet by Colin Howe under Apache license.

Install
=======

    cd gevent_viz
    python setup.py install

Usage
=====

    gevent_viz run yourmodule
    gevent_viz html > yourfile.html

License
=======

    Copyright 2011 Colin Howe (http://www.colinhowe.co.uk @colinhowe)
    Copyright 2012 Stephen Diehl (stephen.m.diehl@gmail.com)

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
