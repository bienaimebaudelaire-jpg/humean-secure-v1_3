# modules/humean_core/gateway/humean_gateway_v2.py
import json
import sys
from pathlib import Path

# Importer la mémoire adaptive
sys.path.append(str(Path(__file__).parent.parent))
from memory.adaptive_memory import AdaptiveMemory

class HumeanGatewayV2:
    """Gateway HUMEAN v2 avec mémoire intégrée"""
    
    def __init__(self):
        self.energy_log = []
        self.module_registry = {}
        self.memory_system = AdaptiveMemory(max_entries=100)
        print("🧠 HUMEAN Gateway v2 initialized with Adaptive Memory")
    
    def register_cognitive_module(self, name, capabilities):
        """Enregistrer un module cognitif HUMEAN"""
        self.module_registry[name] = {
            "capabilities": capabilities,
            "energy_cost": 0.0,
            "activation_count": 0
        }
        print(f"✅ HUMEAN Module registered: {name}")
        
        # Mémoriser l'enregistrement
        self.memory_system.store(
            f"Module {name} registered with capabilities: {capabilities}",
            emotional_weight=0.3,
            cognitive_importance=0.7
        )
        return True
    
    def process_with_cognitive_layer(self, query):
        """Traiter avec mémoire contextuelle"""
        print(f"⚡ HUMEAN Processing: {query}")
        
        # 1. Rappeler le contexte pertinent
        context = self.memory_system.recall(query, max_results=3)
        
        # 2. Traitement cognitif avec contexte
        processed_result = self._cognitive_processing(query, context)
        
        # 3. Calcul des métriques énergétiques
        energy_metrics = self._calculate_energy_metrics(processed_result, len(context))
        
        # 4. Mémoriser l'interaction
        self._store_interaction(query, processed_result, energy_metrics, context)
        
        return {
            "content": processed_result,
            "energy_metrics": energy_metrics,
            "active_modules": list(self.module_registry.keys()),
            "context_used": len(context),
            "humean_version": "0.2",
            "status": "success"
        }
    
    def _cognitive_processing(self, query, context):
        """Traitement cognitif avec contexte"""
        context_summary = [mem["event"] for mem in context] if context else ["No relevant context"]
        
        return {
            "original_query": query,
            "processed_by": "HUMEAN Cognitive Layer v2",
            "context_used": context_summary,
            "analysis": f"Cognitive analysis with {len(context)} context memories",
            "modules_activated": len(self.module_registry)
        }
    
    def _calculate_energy_metrics(self, result, context_size):
        """Calcul des métriques énergétiques avec contexte"""
        complexity = len(str(result)) / 1000
        modules_used = len(self.module_registry)
        context_factor = 1.0 + (context_size * 0.1)  # Plus de contexte = plus d'énergie
        
        return {
            "free_energy": round(complexity * modules_used * context_factor, 4),
            "cognitive_load": round(complexity, 4),
            "efficiency_score": round(1.0 / (complexity + 0.1), 4),
            "modules_active": modules_used,
            "context_memories_used": context_size
        }
    
    def _store_interaction(self, query, result, metrics, context):
        """Stockage de l'interaction complète"""
        interaction_entry = {
            "query": query,
            "result": result,
            "energy_used": metrics["free_energy"],
            "context_size": len(context),
            "modules_involved": list(self.module_registry.keys())
        }
        
        # Stocker avec pondération énergétique
        importance = min(1.0, metrics["free_energy"] * 2)  # Normaliser l'importance
        self.memory_system.store(
            f"Interaction: {query} -> {result['analysis']}",
            emotional_weight=0.5,
            cognitive_importance=importance
        )
        
        print(f"💾 Interaction stored (importance: {importance})")
    
    def get_system_status(self):
        """Statut complet du système HUMEAN"""
        memory_stats = self.memory_system.get_stats()
        
        return {
            "modules_registered": len(self.module_registry),
            "memory_entries": memory_stats["total_memories"],
            "avg_memory_energy": memory_stats["avg_energy"],
            "total_energy_used": sum(entry["energy_used"] for entry in self.energy_log),
            "gateway_version": "HUMEAN v0.2",
            "memory_stats": memory_stats
        }

# TEST DU GATEWAY V2
if __name__ == "__main__":
    print("🚀 INITIALISATION HUMEAN GATEWAY v2...")
    
    # Initialiser le gateway v2
    gw = HumeanGatewayV2()
    
    # Enregistrer les modules cognitifs
    gw.register_cognitive_module("language_processor", ["text_analysis", "semantic_processing"])
    gw.register_cognitive_module("memory_controller", ["short_term", "associative_recall"])
    gw.register_cognitive_module("ethics_validator", ["value_alignment", "harm_prevention"])
    
    print("\n🔧 TESTING COGNITIVE PROCESSING WITH MEMORY...")
    
    # Tester avec différents types de requêtes
    test_queries = [
        "Hello HUMEAN - testing memory integration",
        "What is energy minimization?",
        "How does adaptive memory work?"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n📝 Test {i}: {query}")
        result = gw.process_with_cognitive_layer(query)
        print(f"   ⚡ Energy: {result['energy_metrics']['free_energy']}")
        print(f"   🧠 Modules: {result['active_modules']}")
        print(f"   📚 Context used: {result['context_used']} memories")
    
    print(f"\n📊 SYSTÈME HUMEAN v2 - STATUT FINAL:")
    status = gw.get_system_status()
    for key, value in status.items():
        if key != "memory_stats":
            print(f"   {key}: {value}")
    
    print(f"\n🧠 MEMORY SYSTEM:")
    for key, value in status["memory_stats"].items():
        print(f"   {key}: {value}")
    
    print("\n✅ HUMEAN GATEWAY v2 WITH MEMORY OPERATIONNEL! 🎯")
