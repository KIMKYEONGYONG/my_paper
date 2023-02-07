import UIKit

protocol TopicHomeModelProtocol: AnyObject{
    func topicItemsDownloaded(items: NSArray)
}


class TopicHomeModel: NSObject {

    // properties
    weak var delegate: TopicHomeModelProtocol!
    
    var data = Data()
    
    let urlPath: String = "https://jbit.bufs.ac.kr/~rlaruddyd1/jlv/IOS/topic.php"
    
    /*
    let postUrl = NSURL(string: "https://jbit.bufs.ac.kr/~rlaruddyd1/jlv/IOS/topic.php")
    */
    
    func downloaditems(levelId: String) {
        
        /*
        var request = URLRequest(url: postUrl! as URL)
        request.httpMethod = "POST"
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        request.addValue("application/json", forHTTPHeaderField: "Accept")
        
        let password = "72ak378D"
        
        var postDataString =  "secretWord=\(password)"
        postDataString += "&levelId=\(levelId)"
        
        request.httpBody = postDataString.data(using: String.Encoding.utf8)
        */
        
        let password = "72ak378D"
        var dataString = "?secretWord=\(password)"
        dataString += "&levelId=\(levelId)"
      
        let url:URL = URL(string: urlPath + dataString)!


        let defalutSession = Foundation.URLSession(configuration: URLSessionConfiguration.default)


        let task = defalutSession.dataTask(with: url){ (data, response, error) in
            if error != nil {
                print("Failed to download data")
            }else{
                print("Topic Data downloaded")
                self.parseJSON(data!)
            }
            
        }
        
        task.resume()
        /*
        
        let task = URLSession.shared.dataTask(with: request as URLRequest){ (data, response, error) -> Void in
            
            if error != nil{
                print("Failed to download data")
            }else{
                print("Topic Data downloaded")
                self.parseJSON(data!)
            }
        }
        
        task.resume()
         */
        
    }
    
    func parseJSON(_ data:Data){
        var jsonResult = NSArray()
        
        do {
            jsonResult = try JSONSerialization.jsonObject(with: data, options: JSONSerialization.ReadingOptions.allowFragments) as! NSArray
        } catch let error as NSError {
            print(error)
            return
        }
        
        var jsonElement = NSDictionary()
        let topics = NSMutableArray()
        
        for i in 0..<jsonResult.count{
            jsonElement = jsonResult[i] as! NSDictionary
            
            let topic = TopicModel()
            
            if let topicName = jsonElement["topic_name"] as? String,
               let topicId = jsonElement["topic_id"] as? String {
                topic.topicName = topicName
                topic.topicId = topicId
            }
            
            topics.add(topic)
            
        }
        
        DispatchQueue.main.async(execute: { ()->Void in
            
            self.delegate.topicItemsDownloaded(items: topics)
            
        })
        
    }
    
}
