use v6;
grammar AmplGrammar
{
  rule TOP { (<Line> ;)* }
  rule Line { <Assgn> | <AssgnFn> }
  rule AssgnFn { <Var> \( <FunctionHead> \) = <Final> } 
  token ws { (\h | \s)* }
}
