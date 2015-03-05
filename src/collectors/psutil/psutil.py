# coding=utf-8

"""

"""

import diamond.collector
import psutil
import re

class PsutilCollector(diamond.collector.Collector):

    def get_default_config_help(self):
        config_help = super(PsutilCollector, self).get_default_config_help()
        config_help.update({
        })
        return config_help

    def get_default_config(self):
        """
        Returns the default collector settings
        """
        config = super(PsutilCollector, self).get_default_config()
        config.update({
            'name': '.*',
            'exe': '.*',
            'cwd': '.*',
            'cmdline': '.*',
            'status': '.*.',
            'username': '.*',
            })
        return config

    def collect(self):
        """ Overrides the Collector.collect method
        """
        for pid in psutil.pids():
            p = psutil.Process(pid)
            if not re.match(self.config['name'], p.name):
                continue
            if not re.match(self.config['exe'], p.exe):
                continue
            if not re.match(self.config['cwd'], p.cwd):
                continue
            if not re.match(self.config['cmdline'], " ".join(p.cmdline)):
                continue
            if not re.match(self.config['status'], p.status):
                continue
            if not re.match(self.config['username'], p.username):
                continue
        # Set Metric Name
        metric_prefix = self.config['metric_format'] % self.__dict__
        # Publish CPU stat
        self.publish("%s.cpu.percent" % metric_prefix, p.cpu_percent())
