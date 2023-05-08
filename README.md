# MacOS local code completion with VSCode HF Code Autocomplete plugin
I wanted to see if I could come up with a super simple local server that I could
point the plugin at for use on my m2 macbook air. While I could get something
working using CPU I couldn't get it working using mps.

It's slow so it's not really usable but it was a fun experiment.

Model is bigcode/santacoder

## Input
The HF plugin sends a request like this:
```json
{
  "inputs": "public class Foo {\n    public static void main(String... args) {\n        ",
  "parameters": {
    "max_new_tokens": 60,
    "temperature": 0.2,
    "do_sample": true,
    "top_p": 0.95,
    "stop": [
      "<|endoftext|>"
    ]
  }
}
```

## Output
The output is expected to be an object with a generated_text key:
```json
{
    "generated_text": "code completion text go here"
}
```
