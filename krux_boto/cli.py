# -*- coding: utf-8 -*-
#
# © 2015 Krux Digital, Inc.
#

#
# Standard libraries
#

from __future__ import absolute_import

#
# Third party libraries
#

import boto

#
# Internal libraries
#

import krux.cli
from krux_boto.boto import add_boto_cli_arguments, get_boto, NAME


class Application(krux.cli.Application):

    def __init__(self, name=NAME):
        # Call to the superclass to bootstrap.
        super(Application, self).__init__(name=name)

        self.boto = get_boto(self.args, self.logger, self.stats)

    def add_cli_arguments(self, parser):
        super(Application, self).add_cli_arguments(parser)

        # add the arguments for boto
        add_boto_cli_arguments(parser)

    def run(self):
        region = self.boto.ec2.get_region(self.boto.cli_region)
        ec2 = self.boto.connect_ec2(region=region)

        self.logger.warn('Connected to region: %s', region.name)
        for r in ec2.get_all_regions():
            self.logger.warn('Region: %s', r.name)


def main():
    app = Application()
    with app.context():
        app.run()


# Run the application stand alone
if __name__ == '__main__':
    main()
