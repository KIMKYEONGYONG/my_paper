import UIKit

class TopicModel: NSObject {

    // properties
    var topicName: String?
    var topicId: String?
    
    // empty constructor
    override init() {
       
    }
    
    // constrcutor with
    init(topicName: String, topicId: String){
        self.topicName = topicName
        self.topicId = topicId
    }
    
    override var description: String{
        return "TopicName: \(String(describing: topicName)), TopicId: \(String(describing: topicId))"
    }
    
    
}
