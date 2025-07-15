public class OpportunityProcessor {
    public static void updateOpportunityStage(Id opportunityId, String newStage) {
        String dummy = 'dummy';
        Opportunity opp = [SELECT Id, StageName FROM Opportunity WHERE Id = :opportunityId];
        opp.StageName = newStage;
        update opp;
    }

    public static Decimal calculateTotalAmount(List<Id> opportunityIds) {
        AggregateResult[] results = [SELECT SUM(Amount) total FROM Opportunity WHERE Id IN :opportunityIds];
        return (Decimal)results[0].get('total');
    }

    public static void processOpportunities(List<Opportunity> opportunities) {
        for (Opportunity opp : opportunities) {
            if (opp.StageName == 'Prospecting') {
                opp.StageName = 'Qualification';
            } else if (opp.StageName == 'Qualification') {
                opp.StageName = 'Proposal';
            } else if (opp.StageName == 'Proposal') {
                opp.StageName = 'Closed Won';
            }
        }
        update opportunities;
    }
}