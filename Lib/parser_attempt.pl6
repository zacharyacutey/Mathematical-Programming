use v6;
grammar AmplGrammar
{
  rule TOP { (<Line> ;)* }
  rule Line { <Assgn> | <AssgnFn> }
  rule AssgnFn { <Var> \( <FunctionHead> \) = <Final> }
  rule Assgn { <Var> = <Final> }
  rule Var { } #Temporary
  rule Final { } #"
  rule FunctionHead { } #"
  token ws { (\h | \s)* }
}
