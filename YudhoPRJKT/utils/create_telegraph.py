from telegraph import Telegraph

class CreateTelegraph:
  def __init__(self, title: str,short_name: str, content: str):
    t = Telegraph()
    t.create_account(short_name=short_name)
    r = t.create_page(
      title,
      html_content=content,
    )
    return r["url"]