from playwright.sync_api import Page, expect

def test_iframe(page:Page):
    page.goto("https://the-internet.herokuapp.com/frames")
    page.get_by_role("link", name="iFrame").click()
    
    frame = page.frame_locator("#mce_0_ifr")
    editor = frame.locator("#tinymce") 
    
    expect(editor).to_have_text("Your content goes here.")
    
    the_text = "Learning Playwright with Python"
    editor.fill(the_text)
    
    expect(editor).to_have_text(the_text)

def test_netsted_frames(page:Page):
    page.goto("https://the-internet.herokuapp.com/frames")
    page.get_by_role("link", name="Nested Frames").click()
    
    top_frame = page.frame_locator("frame[name='frame-top']")
    
    left_frame = top_frame.frame_locator("frame[name='frame-left']")
    expect(left_frame.locator("body")).to_have_text("LEFT")
    
    middle_frame = top_frame.frame_locator("frame[name='frame-middle']")
    expect(middle_frame.locator("#content")).to_have_text("MIDDLE")
    
    bottom_frame = page.frame_locator("frame[name='frame-bottom']")
    expect(bottom_frame.locator("body")).to_have_text("BOTTOM")