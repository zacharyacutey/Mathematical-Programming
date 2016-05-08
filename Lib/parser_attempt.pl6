use v6;
grammar AmplGrammar
{
  rule TOP { (<Line> \; )* }
  rule Line { <Assgn> | <AssgnFn> }
  rule AssgnFn { <Var> \( <FunctionHead> \) \= <Final> }
  rule Assgn { <Var> \= <Final> }
  rule Final { <Ite> | <Var> <FinalS> <Final> }
  rule Ite { . }
  rule Var { . }
  rule FinalS { . }
  rule FunctionHead { . }
  token ws { (\h | \s)* }
}
