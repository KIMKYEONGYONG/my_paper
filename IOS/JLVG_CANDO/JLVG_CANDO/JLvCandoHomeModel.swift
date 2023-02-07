import UIKit

protocol JLvCandoHomeModelProtocol: AnyObject{
    func jlvCandoItemsDownloaded(items: NSArray)
}

class JLvCandoHomeModel: NSObject {
    
    weak var delegate: JLvCandoHomeModelProtocol!
    
    var data = Data()
    
    let urlPath: String = "https://jbit.bufs.ac.kr/~rlaruddyd1/jlv/IOS/result.php"
    
    func downloaditems(sentence: String, keyword: String) {
        
        let password = "72ak378D"
        var dataString = "?secretWord=\(password)"
        dataString += "&sentence=\(sentence)&keyword=\(keyword)"
        let urlStr = urlPath + dataString
        print(urlStr)
        guard let encodeStr = urlStr.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) else { return}
        
        let url:URL = URL(string: encodeStr)!
        
        
        let defalutSession = Foundation.URLSession(configuration: URLSessionConfiguration.default)
        
        
        let task = defalutSession.dataTask(with: url){ (data, response, error) in
            if error != nil {
                print("Failed to download data")
            }else{
                print("JLV Cando Data downloaded")
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
            return
        }
        
        var jsonElement = NSDictionary()
        let jlvCandos = NSMutableArray()
        
        for i in 0..<jsonResult.count{
            jsonElement = jsonResult[i] as! NSDictionary
            
            let jlvCando = JLvCandoModel()
            
            if let result = jsonElement["result"] as? String, let percent = jsonElement["percent"] as? String {
                jlvCando.result = result
                jlvCando.percent = percent
                
            }
            
            jlvCandos.add(jlvCando)
            
        }
        
        DispatchQueue.main.async(execute: { ()->Void in
            
            self.delegate.jlvCandoItemsDownloaded(items: jlvCandos)
            
        })
        
    }
    
}
