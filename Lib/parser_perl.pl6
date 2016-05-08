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
  rule Union { <Int> | <Union> <UnionS> <Int> }
  rule UnionS { \\ | ∪ }
  rule Int { <NumE> | <Int> ∩ <NumE> }
  rule NumE { <NumC> <NumEH>* }
  rule NumEH { <NumES> <NumC> }
  rule NumES { ≟ | ≠ }
  rule NumC { <Add> <NumCH>* }
  rule NumCH { <NumCS> <Add> }
  rule NumCS { \< | \> | ≤ | ≥ }
  rule Add { <Mul> | <Mul> <AddS> <Mul> }
  rule AddS { \- | \+ }
  rule Mul { <Exp> | <Mul> <MulS> <Exp> }
  rule MulS { × | ÷ | \% }
  rule Exp { <Unary> | <Unary> \^ <Exp> }
  rule Unary { <Atom> | <UnaryS> <Unary> }
  rule UnaryS { \~ | ∔ | ∸ | ∁ | ℑ | ℜ | ∋ | ω }
  token ws { (\h | \s)* }
}
