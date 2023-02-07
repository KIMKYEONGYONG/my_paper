import UIKit

protocol HomeModelProtocol: AnyObject{
    func levelItemDownloaded(items: NSArray)
}


class HomeModel: NSObject {

    // properties
    weak var delegate: HomeModelProtocol!
    
    var data = Data()
    
    let urlPath: String = "https://jbit.bufs.ac.kr/~rlaruddyd1/jlv/IOS/level.php"
    
    func downloaditems() {
        let url:URL = URL(string: urlPath)!
        let defalutSession = Foundation.URLSession(configuration: URLSessionConfiguration.default)
        
        
        let task = defalutSession.dataTask(with: url){ (data, response, error) in
            if error != nil {
                print("Failed to download data")
            }else{
                print("Level Data downloaded")
                self.parseJSON(data!)
            }
            
        }
        
        task.resume()
    }
    
    func parseJSON(_ data:Data){
        var jsonResult = NSArray()
        
        do {
            jsonResult = try JSONSerialization.jsonObject(with: data, options: JSONSerialization.ReadingOptions.allowFragments) as! NSArray
        } catch let error as NSError {
            print(error)
        }
        
        var jsonElement = NSDictionary()
        let levels = NSMutableArray()
        
        for i in 0..<jsonResult.count{
            jsonElement = jsonResult[i] as! NSDictionary
            
            let level = LevelModel()
            
            if let levelName = jsonElement["level_name"] as? String,
               let levelId = jsonElement["level_id"] as? String {
                level.levelName = levelName
                level.levelId = levelId
            }
            
            levels.add(level)
            
        }
        
        DispatchQueue.main.async(execute: { ()->Void in
            
            self.delegate.levelItemDownloaded(items: levels)
            
        })
        
    }
    
}
