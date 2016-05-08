use v6;
grammar AmplGrammar
{
  rule TOP { (<Line> \; )* }
  rule Line { <Assgn> | <AssgnFn> }
  rule AssgnFn { <Var> \( <FunctionHead> \) \= <Final> }
  rule Assgn { <Var> \= <Final> }
  rule Final { <Ite> | <Var> <FinalS> <Final> }
  rule FinalS { Π | Σ }
  rule Ite { <Or> | <Or> → <Final> ↛ <Ite> } 
  token ws { (\h | \s)* }
}
