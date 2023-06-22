import feedgen.feed

from fastapi import Query, Request, Response

from api.router import router
from indexer import service, schemas


@router.get("/rss", name="rss_feed")
def post_feed(
    request: Request,
    title: str | None = Query(None),
    author: str | None = Query(None),
    size: int = Query(50),
):
    results = service.search_post(
        search_params=schemas.PostSearch(title=title, author=author, count=size)
    )
    feed = feedgen.feed.FeedGenerator()
    feed.title("Posts RSS")
    feed.link(href=str(request.url_for("rss_feed")), rel="self")
    feed.description("Latest Posts")

    for submission in results:
        entry = feed.add_entry()
        entry.guid(str(submission.id))
        entry.title(submission.title)
        entry.source(submission.author)
        entry.link(href=str(request.url_for("post_detail", post_id=submission.id)))
        entry.pubDate(submission.created_at)

    return Response(content=feed.rss_str(pretty=True), media_type="application/xml")
