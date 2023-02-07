import UIKit

class JLvCandoModel: NSObject {

    
    // properties
    var result: String?
    var percent: String?
    
    override init() {
        
    }
    
    init(result: String, percent: String){
        self.result = result
        self.percent = percent
    }

    override var description: String{
        return "Result: \(result!), Percent: \(percent!)"
    }
}
