import React, { useState, useEffect } from 'react';
import { useAuth } from '@/contexts/AuthContext.jsx';
import pb from '@/lib/pocketbaseClient';
import { analyzeBehavior } from '@/lib/BehaviorAnalyzer.js';
import SimulationResult from '@/components/SimulationResult.jsx';
import { Button } from '@/components/ui/button';
import { Textarea } from '@/components/ui/textarea';
import { Label } from '@/components/ui/label';
import { Sparkles, Loader2 } from 'lucide-react';
import { toast } from 'sonner';

const DecisionSimulator = () => {
  const { currentUser } = useAuth();
  const [scenario, setScenario] = useState('');
  const [loading, setLoading] = useState(false);
  const [simulations, setSimulations] = useState([]);
  const [behaviorAnalysis, setBehaviorAnalysis] = useState(null);

  useEffect(() => {
    if (currentUser) {
      loadSimulations();
      loadBehaviorProfile();
    }
  }, [currentUser]);

  const loadSimulations = async () => {
    try {
      const records = await pb.collection('simulations').getFullList({
        filter: `userId = "${currentUser.id}"`,
        sort: '-created',
        $autoCancel: false
      });
      setSimulations(records);
    } catch (error) {
      console.error('Error loading simulations:', error);
    }
  };

  const loadBehaviorProfile = async () => {
    try {
      const analysis = await analyzeBehavior(currentUser.id);
      setBehaviorAnalysis(analysis);
    } catch (error) {
      console.error('Error loading behavior profile:', error);
    }
  };

  const generatePrediction = (scenario, patterns) => {
    const scenarioLower = scenario.toLowerCase();
    
    if (scenarioLower.includes('buy') || scenarioLower.includes('purchase')) {
      if (patterns.analytical) {
        return {
          prediction: "You will likely research extensively, compare prices across multiple retailers, read reviews, and wait for a sale before making the purchase.",
          reasoning: "Your analytical decision-making pattern suggests you prefer thorough evaluation before committing to purchases.",
          confidence: 87
        };
      } else if (patterns.impulsive) {
        return {
          prediction: "You will probably make the purchase quickly, possibly within the same day, driven by immediate desire rather than extensive research.",
          reasoning: "Your spontaneous nature indicates you tend to act on impulse when something catches your interest.",
          confidence: 82
        };
      }
    }

    if (scenarioLower.includes('job') || scenarioLower.includes('career')) {
      if (patterns.planner) {
        return {
          prediction: "You will create a detailed plan with milestones, research the company thoroughly, prepare extensively for interviews, and carefully evaluate the offer.",
          reasoning: "Your planning-oriented approach suggests you'll take a structured, methodical path to this career decision.",
          confidence: 85
        };
      } else if (patterns.riskTaker) {
        return {
          prediction: "You will likely take the leap quickly if the opportunity excites you, even if it involves uncertainty or risk.",
          reasoning: "Your adventurous spirit indicates you're comfortable with calculated risks in pursuit of growth.",
          confidence: 79
        };
      }
    }

    if (scenarioLower.includes('social') || scenarioLower.includes('event') || scenarioLower.includes('party')) {
      if (patterns.social) {
        return {
          prediction: "You will enthusiastically attend, arrive early, engage with many people, and likely stay until the end.",
          reasoning: "Your social nature suggests you thrive in group settings and enjoy meeting new people.",
          confidence: 88
        };
      } else {
        return {
          prediction: "You might attend but prefer smaller conversations, arrive fashionably late, and leave earlier than most.",
          reasoning: "Based on your preferences, you likely enjoy social interaction in moderation but value your personal time.",
          confidence: 76
        };
      }
    }

    return {
      prediction: "Based on your behavior patterns, you will approach this situation with a balanced perspective, considering both practical factors and personal preferences before deciding.",
      reasoning: "Your decision-making style suggests you weigh multiple factors and take time to evaluate options.",
      confidence: 72
    };
  };

  const handleSimulate = async (e) => {
    e.preventDefault();
    if (!scenario.trim() || loading) return;

    if (!behaviorAnalysis || behaviorAnalysis.totalResponses === 0) {
      toast.error('Complete the onboarding questionnaire first to enable predictions');
      return;
    }

    setLoading(true);

    try {
      await new Promise(resolve => setTimeout(resolve, 1200));

      const { prediction, reasoning, confidence } = generatePrediction(
        scenario,
        behaviorAnalysis.patterns
      );

      const record = await pb.collection('simulations').create({
        userId: currentUser.id,
        scenario: scenario.trim(),
        prediction,
        reasoning,
        confidence
      }, { $autoCancel: false });

      setSimulations(prev => [record, ...prev]);
      setScenario('');
      toast.success('Simulation complete');
    } catch (error) {
      console.error('Error creating simulation:', error);
      toast.error('Failed to run simulation');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-8">
      <div className="bg-gray-900/50 rounded-2xl p-6 border border-gray-800">
        <form onSubmit={handleSimulate} className="space-y-4">
          <div>
            <Label htmlFor="scenario" className="text-gray-200 font-medium mb-2 block">
              Describe a scenario or decision
            </Label>
            <Textarea
              id="scenario"
              value={scenario}
              onChange={(e) => setScenario(e.target.value)}
              placeholder="Example: I'm considering buying a new laptop for $1,200. Should I buy it now or wait?"
              className="bg-gray-800 border-gray-700 text-white placeholder:text-gray-500 min-h-[120px]"
              disabled={loading}
            />
          </div>

          <Button
            type="submit"
            disabled={!scenario.trim() || loading}
            className="w-full bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white"
          >
            {loading ? (
              <>
                <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                Analyzing...
              </>
            ) : (
              <>
                <Sparkles className="w-4 h-4 mr-2" />
                Run Simulation
              </>
            )}
          </Button>
        </form>
      </div>

      <div>
        <h2 className="text-xl font-bold text-white mb-4" style={{ letterSpacing: '-0.02em' }}>
          Simulation History
        </h2>
        <div className="space-y-4">
          {simulations.length === 0 ? (
            <div className="text-center py-12 bg-gray-900/30 rounded-2xl border border-gray-800">
              <p className="text-gray-400">No simulations yet</p>
              <p className="text-sm text-gray-500 mt-2">
                Enter a scenario above to see how your digital twin predicts you'll respond
              </p>
            </div>
          ) : (
            simulations.map((sim) => (
              <SimulationResult
                key={sim.id}
                scenario={sim.scenario}
                prediction={sim.prediction}
                reasoning={sim.reasoning}
                confidence={sim.confidence}
                timestamp={sim.created}
              />
            ))
          )}
        </div>
      </div>
    </div>
  );
};

export default DecisionSimulator;