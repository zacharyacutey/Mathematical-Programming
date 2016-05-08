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
  rule FinalS { Π | Σ } #Moment of unicode truth!
  rule FunctionHead { . }
  token ws { (\h | \s)* }
}
