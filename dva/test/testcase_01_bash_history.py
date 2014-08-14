""" This module contains testcase_01_bash_history test """
from testcase import Testcase


class testcase_01_bash_history(Testcase):
    """
    Ensure /root/.bash_history file is empty
    """
    stages = ['stage1']
    tags = ['default']

    # pylint: disable=W0613
    def test(self, connection, params):
        """ Perform test """

        self.ping_pong(connection, '[ ! -f ~/.bash_history ] && echo 0 || cat ~/.bash_history | wc -l', '\r\n0\r\n')

        return self.log
