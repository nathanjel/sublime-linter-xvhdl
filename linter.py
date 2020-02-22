from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class XVHDL(Linter):
    cmd = ('xvhdl', '--2008', '--nolog')
    tempfile_suffix = '-'
    regex = r'^(?P<error>ERROR): \[.*?(?P<code>[0-9-]+)\]\s(?P<message>.*)\s\[(?P<path>.*):(?P<line>\d+).*$'
    multiline = False
    defaults = {
        'selector': 'source.vhdl'
    }
