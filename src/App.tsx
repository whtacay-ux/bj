/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Gamepad2, Code2, BookOpen, User, Coins, RefreshCw, Hand, Info } from 'lucide-react';
import { GAME_SOURCE_CPP, PYTHON_SCRIPT } from './constants';

// --- Types ---
type Card = {
  suit: 'hearts' | 'diamonds' | 'clubs' | 'spades';
  value: string;
  rank: number;
};

type GameState = 'betting' | 'playing' | 'dealer-turn' | 'result';

// --- Helpers ---
const SUITS = ['hearts', 'diamonds', 'clubs', 'spades'] as const;
const VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'];

const createCard = (): Card => {
  const suit = SUITS[Math.floor(Math.random() * SUITS.length)];
  const value = VALUES[Math.floor(Math.random() * VALUES.length)];
  let rank = VALUES.indexOf(value) + 1;
  if (rank > 10) rank = 10;
  if (value === 'A') rank = 11;
  return { suit, value, rank };
};

const calculateScore = (hand: Card[]) => {
  let score = hand.reduce((total, card) => total + card.rank, 0);
  let aces = hand.filter(card => card.value === 'A').length;
  while (score > 21 && aces > 0) {
    score -= 10;
    aces--;
  }
  return score;
};

// --- Components ---

const Metin2Window = ({ title, children, onClose }: { title: string; children: React.ReactNode; onClose?: () => void }) => (
  <div className="relative w-full max-w-2xl bg-[#1a1510] border-2 border-[#8b6b4a] shadow-2xl rounded-sm overflow-hidden flex flex-col min-h-[500px]">
    {/* Title Bar */}
    <div className="bg-[#2d2419] border-b border-[#8b6b4a] p-2 flex justify-between items-center px-4">
      <span className="text-[#e2d4b6] font-serif font-bold text-sm tracking-wide uppercase">{title}</span>
      {onClose && (
        <button onClick={onClose} className="w-5 h-5 bg-[#8b6b4a] flex items-center justify-center text-xs text-white hover:bg-[#a67d58] transition-colors">
          ×
        </button>
      )}
    </div>
    {/* Decorative Border Internal */}
    <div className="flex-1 p-6 relative">
      <div className="absolute inset-2 border border-[#8b6b4a]/30 pointer-events-none" />
      {children}
    </div>
  </div>
);

const CardComponent = ({ card, hidden }: { card: Card; hidden?: boolean }) => (
  <motion.div
    initial={{ scale: 0.5, rotateY: 180, opacity: 0 }}
    animate={{ scale: 1, rotateY: hidden ? 180 : 0, opacity: 1 }}
    transition={{ type: 'spring', stiffness: 260, damping: 20 }}
    className="w-20 h-28 md:w-24 md:h-34 relative preserve-3d"
  >
    {/* Back */}
    <div className="absolute inset-0 bg-[#3d2e1f] border-2 border-[#8b6b4a] rounded-md backface-hidden flex items-center justify-center">
      <div className="w-full h-full p-2">
        <div className="w-full h-full border border-[#8b6b4a]/50 rounded-sm flex items-center justify-center bg-[#2a1d12]">
          <RefreshCw className="text-[#8b6b4a]/40 w-8 h-8 rotate-45" />
        </div>
      </div>
    </div>
    {/* Front */}
    {!hidden && (
      <div className="absolute inset-0 bg-white border-2 border-[#8b6b4a] rounded-md backface-hidden flex flex-col items-center justify-center text-[#1a1510]">
        <span className={`text-xl font-bold font-serif \${card.suit === 'hearts' || card.suit === 'diamonds' ? 'text-red-600' : 'text-slate-900'}`}>{card.value}</span>
        <div className="opacity-80">
          {card.suit === 'hearts' && '♥'}
          {card.suit === 'diamonds' && '♦'}
          {card.suit === 'clubs' && '♣'}
          {card.suit === 'spades' && '♠'}
        </div>
      </div>
    )}
  </motion.div>
);

export default function App() {
  const [tab, setTab] = useState<'demo' | 'code' | 'guide'>('demo');
  const [codeTab, setCodeTab] = useState<'cpp' | 'py'>('cpp');

  // Game Logic
  const [gameState, setGameState] = useState<GameState>('betting');
  const [playerHand, setPlayerHand] = useState<Card[]>([]);
  const [dealerHand, setDealerHand] = useState<Card[]>([]);
  const [balance, setBalance] = useState(5000000); // 5m yang
  const [bet, setBet] = useState(100000);
  const [message, setMessage] = useState('');

  const startGame = () => {
    if (balance < bet) return;
    setBalance(prev => prev - bet);
    const p1 = createCard();
    const d1 = createCard();
    const p2 = createCard();
    const d2 = createCard();
    setPlayerHand([p1, p2]);
    setDealerHand([d1, d2]);
    setGameState('playing');
    setMessage('');
  };

  const hit = () => {
    const newCard = createCard();
    const newHand = [...playerHand, newCard];
    setPlayerHand(newHand);
    if (calculateScore(newHand) > 21) {
      endGame('bust');
    }
  };

  const stand = () => {
    setGameState('dealer-turn');
  };

  useEffect(() => {
    if (gameState === 'dealer-turn') {
      const dealerThink = async () => {
        let currentDealerHand = [...dealerHand];
        while (calculateScore(currentDealerHand) < 17) {
          await new Promise(r => setTimeout(r, 800));
          currentDealerHand = [...currentDealerHand, createCard()];
          setDealerHand(currentDealerHand);
        }
        
        const dScore = calculateScore(currentDealerHand);
        const pScore = calculateScore(playerHand);

        if (dScore > 21 || pScore > dScore) {
          endGame('win');
        } else if (pScore < dScore) {
          endGame('lose');
        } else {
          endGame('draw');
        }
      };
      dealerThink();
    }
  }, [gameState]);

  const endGame = (result: 'win' | 'lose' | 'draw' | 'bust') => {
    setGameState('result');
    if (result === 'win') {
      setBalance(prev => prev + bet * 2);
      setMessage('TEBRİKLER! KAZANDINIZ.');
    } else if (result === 'draw') {
      setBalance(prev => prev + bet);
      setMessage('BERABERE! BAHİS İADE EDİLDİ.');
    } else {
      setMessage(result === 'bust' ? 'İFLAS! KAYBETTİNİZ.' : 'KAYBETTİNİZ.');
    }
  };

  return (
    <div className="min-h-screen bg-[#0c0907] text-[#e2d4b6] font-sans selection:bg-[#8b6b4a] selection:text-white pb-20">
      {/* Header */}
      <header className="bg-[#1a1510] border-b border-[#8b6b4a] p-4 flex flex-col md:flex-row items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-[#2d2419] border border-[#8b6b4a] rounded">
            <Coins className="text-[#d4af37] w-6 h-6" />
          </div>
          <div>
            <h1 className="text-xl font-bold font-serif uppercase tracking-widest text-[#d4af37]">Metin2 Blackjack System</h1>
            <p className="text-xs text-[#8b6b4a] font-mono">Developer Dashboard v1.0.0</p>
          </div>
        </div>
        <nav className="flex gap-2">
          <button
            onClick={() => setTab('demo')}
            className={`flex items-center gap-2 px-4 py-2 rounded transition-all \${tab === 'demo' ? 'bg-[#8b6b4a] text-white' : 'hover:bg-[#2d2419] text-[#8b6b4a]'}`}
          >
            <Gamepad2 size={18} /> Önizleme
          </button>
          <button
            onClick={() => setTab('code')}
            className={`flex items-center gap-2 px-4 py-2 rounded transition-all \${tab === 'code' ? 'bg-[#8b6b4a] text-white' : 'hover:bg-[#2d2419] text-[#8b6b4a]'}`}
          >
            <Code2 size={18} /> Kodlar
          </button>
          <button
            onClick={() => setTab('guide')}
            className={`flex items-center gap-2 px-4 py-2 rounded transition-all \${tab === 'guide' ? 'bg-[#8b6b4a] text-white' : 'hover:bg-[#2d2419] text-[#8b6b4a]'}`}
          >
            <BookOpen size={18} /> Rehber
          </button>
        </nav>
      </header>

      <main className="container mx-auto mt-8 px-4 flex justify-center">
        {tab === 'demo' && (
          <div className="w-full max-w-4xl flex flex-col items-center gap-8">
            <div className="flex items-center gap-6 bg-[#1a1510] p-4 border border-[#8b6b4a] rounded w-full justify-center">
              <div className="flex items-center gap-2">
                <User className="text-[#8b6b4a]" size={20} />
                <span className="font-serif">KARAKTER: <span className="text-white">Admin</span></span>
              </div>
              <div className="w-px h-6 bg-[#8b6b4a]/30" />
              <div className="flex items-center gap-2">
                <Coins className="text-[#d4af37]" size={20} />
                <span className="font-serif text-[#d4af37]">YANG: {balance.toLocaleString()}</span>
              </div>
            </div>

            <Metin2Window title="Blackjack - Şans Oyunu">
              <div className="flex flex-col h-[500px]">
                {/* Dealer Area */}
                <div className="flex-1 flex flex-col items-center justify-center gap-4 relative">
                  <div className="text-[#8b6b4a] uppercase text-xs font-bold tracking-widest bg-[#0c0907]/50 px-3 py-1 rounded">DEALER (ASA)</div>
                  <div className="flex gap-3 min-h-[120px]">
                    <AnimatePresence>
                      {dealerHand.map((card, i) => (
                        <CardComponent key={i} card={card} hidden={i === 1 && gameState === 'playing'} />
                      ))}
                    </AnimatePresence>
                  </div>
                  {gameState === 'dealer-turn' && (
                    <div className="text-lg font-bold text-[#d4af37] font-serif">Skor: {calculateScore(dealerHand)}</div>
                  )}
                </div>

                {/* Info Area */}
                <div className="h-20 flex items-center justify-center border-y border-[#8b6b4a]/20">
                  <div className="text-center">
                    {gameState === 'betting' && <p className="text-[#8b6b4a] animate-pulse uppercase tracking-wider">Bahis miktarını belirleyip oyuna başla</p>}
                    {message && <p className="text-xl font-bold text-[#d4af37] drop-shadow-lg tracking-widest">{message}</p>}
                  </div>
                </div>

                {/* Player Area */}
                <div className="flex-1 flex flex-col items-center justify-center gap-4 relative mt-4">
                  <div className="flex gap-3 min-h-[120px]">
                    <AnimatePresence>
                      {playerHand.map((card, i) => (
                        <CardComponent key={i} card={card} />
                      ))}
                    </AnimatePresence>
                  </div>
                  {(gameState === 'playing' || gameState === 'result') && (
                    <div className="text-lg font-bold text-[#d4af37] font-serif">Skor: {calculateScore(playerHand)}</div>
                  )}
                  <div className="text-[#b49b7d] uppercase text-xs font-bold tracking-widest bg-[#0c0907]/50 px-3 py-1 rounded">OYUNCU</div>
                </div>

                {/* Controls */}
                <div className="mt-8 flex justify-center gap-4">
                  {gameState === 'betting' ? (
                    <div className="flex flex-col items-center gap-4">
                      <div className="flex items-center gap-4 bg-[#0c0907] border border-[#8b6b4a] p-2 rounded">
                        <span className="text-xs text-[#8b6b4a] ml-2">BAHİS:</span>
                        <input
                          type="number"
                          value={bet}
                          onChange={(e) => setBet(Math.min(balance, Math.max(1000, parseInt(e.target.value) || 0)))}
                          className="bg-transparent border-none outline-none text-[#d4af37] font-serif text-lg w-32"
                        />
                      </div>
                      <button
                        onClick={startGame}
                        className="bg-[#8b6b4a] hover:bg-[#a67d58] text-white px-12 py-3 border-2 border-[#b49b7d] rounded uppercase font-bold tracking-widest shadow-lg transition-transform active:scale-95"
                      >
                        OYUNU BAŞLAT
                      </button>
                    </div>
                  ) : gameState === 'playing' ? (
                    <div className="flex gap-4">
                      <button
                        onClick={hit}
                        className="bg-[#2d2419] hover:bg-[#3d2e1f] text-[#d4af37] px-8 py-3 border border-[#8b6b4a] rounded flex items-center gap-2 transition-colors"
                      >
                        <RefreshCw size={18} /> KART ÇEK
                      </button>
                      <button
                        onClick={stand}
                        className="bg-[#2d2419] hover:bg-[#3d2e1f] text-white px-8 py-3 border border-[#8b6b4a] rounded flex items-center gap-2 transition-colors"
                      >
                        <Hand size={18} /> DUR
                      </button>
                    </div>
                  ) : (
                    <button
                      onClick={() => {
                        setGameState('betting');
                        setPlayerHand([]);
                        setDealerHand([]);
                        setMessage('');
                      }}
                      className="bg-[#8b6b4a] hover:bg-[#a67d58] text-white px-8 py-3 border border-[#b49b7d] rounded uppercase font-bold tracking-widest shadow-lg transition-transform active:scale-95"
                    >
                      TEKRAR OYNA
                    </button>
                  )}
                </div>
              </div>
            </Metin2Window>
          </div>
        )}

        {tab === 'code' && (
          <div className="w-full max-w-5xl">
            <div className="flex gap-px mb-1">
              <button
                onClick={() => setCodeTab('cpp')}
                className={`px-6 py-2 rounded-t font-serif text-sm transition-colors \${codeTab === 'cpp' ? 'bg-[#1a1510] text-[#d4af37] border-t border-x border-[#8b6b4a]' : 'bg-[#0c0907] text-[#8b6b4a] hover:bg-[#1a1510]'}`}
              >
                GAME SOURCE (C++)
              </button>
              <button
                onClick={() => setCodeTab('py')}
                className={`px-6 py-2 rounded-t font-serif text-sm transition-colors \${codeTab === 'py' ? 'bg-[#1a1510] text-[#d4af37] border-t border-x border-[#8b6b4a]' : 'bg-[#0c0907] text-[#8b6b4a] hover:bg-[#1a1510]'}`}
              >
                PYTHON (UI)
              </button>
            </div>
            <div className="bg-[#1a1510] border border-[#8b6b4a] rounded-b-lg p-6 overflow-hidden">
               <div className="flex justify-between items-center mb-4">
                 <h3 className="text-[#d4af37] font-serif flex items-center gap-2">
                   <Code2 size={16} /> {codeTab === 'cpp' ? 'blackjack_manager.cpp / .h' : 'uiBlackjack.py'}
                 </h3>
                 <button 
                  onClick={() => navigator.clipboard.writeText(codeTab === 'cpp' ? GAME_SOURCE_CPP : PYTHON_SCRIPT)}
                  className="text-xs bg-[#2d2419] px-3 py-1 border border-[#8b6b4a] rounded hover:text-white transition-colors"
                 >
                   Dosyayı Kopyala
                 </button>
               </div>
               <pre className="text-xs md:text-sm bg-[#0c0907] p-4 rounded border border-[#8b6b4a]/20 overflow-x-auto font-mono text-gray-400">
                 <code>{codeTab === 'cpp' ? GAME_SOURCE_CPP : PYTHON_SCRIPT}</code>
               </pre>
            </div>
          </div>
        )}

        {tab === 'guide' && (
          <div className="w-full max-w-3xl space-y-6">
            <div className="bg-[#1a1510] border border-[#8b6b4a] p-8 rounded-lg">
              <h2 className="text-2xl font-serif text-[#d4af37] mb-6 flex items-center gap-3">
                <BookOpen className="text-[#8b6b4a]" /> KURULUM REHBERİ
              </h2>
              
              <div className="space-y-8">
                <section>
                  <h3 className="text-lg text-[#d4af37] font-serif mb-2 flex items-center gap-2 border-b border-[#8b6b4a]/30 pb-1">
                    <span className="bg-[#8b6b4a] text-white w-6 h-6 rounded-full flex items-center justify-center text-xs">1</span>
                    Server Tarafı (Game Source)
                  </h3>
                  <div className="text-sm text-[#8b6b4a] leading-relaxed space-y-2">
                    <p>• <code className="text-[#d4af37]">blackjack_manager.cpp</code> ve <code className="text-[#d4af37]">.h</code> dosyalarını projenize ekleyin.</p>
                    <p>• <code className="text-[#d4af37]">input_main.cpp</code> içerisinde oyuncudan gelen paketleri (hit, stand, bet) handle edin.</p>
                    <p>• Oyunun durumunu takip etmek için karakter map'ini kullanın.</p>
                  </div>
                </section>

                <section>
                  <h3 className="text-lg text-[#d4af37] font-serif mb-2 flex items-center gap-2 border-b border-[#8b6b4a]/30 pb-1">
                    <span className="bg-[#8b6b4a] text-white w-6 h-6 rounded-full flex items-center justify-center text-xs">2</span>
                    Python Tarafı (Client UI)
                  </h3>
                  <div className="text-sm text-[#8b6b4a] leading-relaxed space-y-2">
                    <p>• <code className="text-[#d4af37]">uiBlackjack.py</code> dosyasını root/uiscript içerisine yerleştirin.</p>
                    <p>• <code className="text-[#d4af37]">game.py</code> içerisinde pencereyi çağıran bir kısayol veya buton ekleyin.</p>
                    <p>• <code className="text-[#d4af37]">net.SendChatPacket</code> yerine imkanınız varsa direkt packet yapısını kullanın.</p>
                  </div>
                </section>

                <section className="bg-[#0c0907]/50 p-4 rounded border border-[#8b6b4a]/20">
                  <h3 className="text-[#d4af37] font-bold text-sm mb-2 flex items-center gap-2">
                    <Info size={16} /> ÖNEMLİ NOT
                  </h3>
                  <p className="text-xs text-[#8b6b4a]">
                    Bu sistem temel mantığı göstermektedir. Canlı bir sunucuda kullanmadan önce kart görsellerini (Ymir work) eklemeniz ve paket güvenliğini (anti-cheat) sağlamanız önerilir.
                  </p>
                </section>
              </div>
            </div>
          </div>
        )}
      </main>

      {/* Background Decor */}
      <div className="fixed top-0 left-0 w-full h-full pointer-events-none opacity-5 flex justify-between px-20">
        <div className="w-1 h-full bg-gradient-to-b from-transparent via-[#8b6b4a] to-transparent" />
        <div className="w-1 h-full bg-gradient-to-b from-transparent via-[#8b6b4a] to-transparent" />
      </div>
    </div>
  );
}
