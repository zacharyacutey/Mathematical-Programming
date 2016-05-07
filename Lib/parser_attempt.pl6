use v6;
grammar AmplGrammar
{
  rule TOP { <line=.Assgn> | <line=.AssgnFn> }
  token ws { (\h | \s)* }
}

class AmplGrammarAction
{
  method TOP($/) {
    $/.make($/);
  }
}
