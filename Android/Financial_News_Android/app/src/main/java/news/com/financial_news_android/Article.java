package news.com.financial_news_android;

import android.os.Parcel;
import android.os.Parcelable;

import com.raizlabs.android.dbflow.annotation.Column;
import com.raizlabs.android.dbflow.annotation.PrimaryKey;
import com.raizlabs.android.dbflow.annotation.Table;
import com.raizlabs.android.dbflow.structure.BaseModel;

/**
 * A model corresponding to table Article
 *
 * Created by Ping He on 2016/6/28.
 */
@Table(database = AppDatabase.class)
public class Article extends BaseModel implements Parcelable {

    public Article() {}

    // id (auto increment)
    @PrimaryKey(autoincrement = true)
    long id;

    // the id of the article
    @Column
    private long articleid;

    // whether this article is liked by user
    @Column
    private String isFav;

    // the title of the article
    @Column
    private String headline;

    // the subtitle of the article
    @Column
    private String subHeadline;

    // article url
    @Column
    private String url;

    // article datetime
    @Column
    private String datetime;

    // article keywords
    @Column
    private String keywords;

    // article content
    @Column
    private String content;

    // user feedback
    @Column
    private int feedback;

    // url of news image
    @Column
    private String image;

    // local image path of news
    @Column
    private String localImage;

    @Column
    private String type;

    // news source
    @Column
    private String source;

    public long getArticleid() {
        return articleid;
    }

    public void setArticleid(long articleid) {
        this.articleid = articleid;
    }

    public String getIsFav() {
        return isFav;
    }

    public void setIsFav(String fav) {
        isFav = fav;
    }

    public int getFeedback() {
        return feedback;
    }

    public void setFeedback(int feedback) {
        this.feedback = feedback;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public String getLocalImage() {
        return localImage;
    }

    public void setLocalImage(String localImage) {
        this.localImage = localImage;
    }

    public String getHeadline() {
        return headline;
    }

    public void setHeadline(String headline) {
        this.headline = headline;
    }

    public String getSubHeadline() {
        return subHeadline;
    }

    public void setSubHeadline(String subHeadline) {
        this.subHeadline = subHeadline;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getDatetime() {
        return datetime;
    }

    public void setDatetime(String datetime) {
        this.datetime = datetime;
    }

    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    @Override
    public int describeContents() {
        return 0;
    }

    // write your object's data to the passed-in Parcel
    @Override
    public void writeToParcel(Parcel out, int flags) {
        out.writeLong(articleid);
        out.writeString(headline);
        out.writeString(subHeadline);
        out.writeString(content);
        out.writeString(image);
        out.writeString(source);
        out.writeString(isFav);
        out.writeString(keywords);
        out.writeString(datetime);
        out.writeInt(feedback);
    }

    // this is used to regenerate your object. All Parcelables must have a CREATOR that implements these two methods
    public static final Parcelable.Creator<Article> CREATOR = new Parcelable.Creator<Article>() {
        public Article createFromParcel(Parcel in) {
            return new Article(in);
        }

        public Article[] newArray(int size) {
            return new Article[size];
        }
    };

    // example constructor that takes a Parcel and gives you an object populated with it's values
    public Article(Parcel in) {
        articleid = in.readLong();
        headline = in.readString();
        subHeadline = in.readString();
        content = in.readString();
        image = in.readString();
        source = in.readString();
        isFav = in.readString();
        keywords = in.readString();
        datetime = in.readString();
        feedback = in.readInt();
    }
}
