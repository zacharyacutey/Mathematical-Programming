use v6;
@f = 1;
grammar AmplGrammar
{
  rule TOP { (<Line> ;)* }
  rule Line { <Assgn> | <AssgnFn> }
  token ws { (\h | \s)* }
}
