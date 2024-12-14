import censurador

palavrasCensuradas = [
    'porra', 'foda', 'fuder', 'merda', 'caralho', 'puta', 'bosta', 
    'cacete', 'desgraça', 'vagabunda', 'vagabundo', 'putaria', 
    'puto', 'fdp', 'pqp', 'cu', 'babaca', 'corno', 'viado', 
    'gayzinho', 'imbecil', 'burro', 'otario', 'palhaço', 'cuzao', 
    'trouxa', 'macaco', 'idiota', 'chupa', 'imbecil', 'nojento', 
    'escroto', 'lixo', 'puta', 'traste', 'meretriz', 'miseravel', 'abusado', 
    'bocozinho', 'otaria', 'cretino', 'cretina', 'idiotice', 
    'vagabundagem', 'corrupto', 'corrupta', 'malandro', 'malandra', 
    'canalha', 'ladrao', 'ladra', 'cachorra', 'cachorro', 'prostituta', 
    'prostituto', 'escoria', 'pilantra', 'safado', 'safada', 'pateta', 
    'mentiroso', 'mentirosa', 'desonesto', 'desonesta', 'covarde', 
    'canalhice', 'zorra', 'antipatico', 'antipatica', 'falsiane', 
    'pistoleiro', 'pistoleira', 'pevertido', 'pervertida', 'depravado'
]

mensagem = input('Digite uma mensagem: ')

mensagemCensurada = censurador.censura(mensagem, palavrasCensuradas)

print(f'\nMensagem enviada: {mensagemCensurada}\n')