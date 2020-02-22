from SublimeLinter.lint import Linter  # or NodeLinter, PythonLinter, ComposerLinter, RubyLinter


class __class__(Linter):
    cmd = 'xvhdl @'
    regex = r'^(?P<error>ERROR): \[.*?(?P<code>[0-9-]+)\]\s(?P<message>.*)\s\[(?P<path>.*):(?P<line>\d+).*$'
    multiline = False
    defaults = {
        'selector': 'source.vhdl'
    }
