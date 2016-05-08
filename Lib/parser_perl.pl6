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
  rule Or { <And> | <Or> ∨ <And> }
  rule And { <SetE> | <And> ∧ <SetE> }
  rule SetE { <SetC> <SetEH>* }
  rule SetEH { <SetES> <SetC> }
  rule SetES { ≡ | ≢ }
  rule SetC { <Union> <SetCH>* }
  rule SetCH { <SetCS> <Union> }
  rule SetCS { ⊂ | ⊃ | ⊆ | ⊇ | ∈ }
  token ws { (\h | \s)* }
}
