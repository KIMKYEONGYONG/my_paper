import UIKit

class JLvModel: NSObject {
    
    // properties
    var sentence: String?
    
    override init() {
        
    }
    
    init(sentence: String){
        self.sentence = sentence
    }

    override var description: String{
        return "Sentence: \(sentence!)"
    }
}
