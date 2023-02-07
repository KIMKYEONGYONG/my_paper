import UIKit

class LevelModel: NSObject {

    // properties
    var levelName: String?
    var levelId: String?
    
    // empty constructor
    override init() {
       
    }
    
    // constrcutor with
    init(levelName: String, levelId: String){
        self.levelName = levelName
        self.levelId = levelId
    }
    
    override var description: String{
        return "LevelName: \(String(describing: levelName)), LevelId: \(String(describing: levelId))"
    }
    
    
}
