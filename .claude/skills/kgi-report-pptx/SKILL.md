---
name: kgi-report-pptx
description: 用凱基證券公司 PPT 模板（16:9、深藍/品牌藍 + 橘紅方塊導言、左上 Logo、底部藍色斜條）製作報告簡報 .pptx。當使用者要做內部報告、策略/系統簡報、晨會或研究報告投影片，或提到「用我的模板」「公司模板」「KGI 模板」時使用。
---

# 凱基報告簡報模板

把使用者的內容套進公司模板，輸出可直接在 PowerPoint 編輯的 .pptx。母片、Logo、頂部藍條、頁碼、頁尾斜條都來自模板，不要自己重畫。

## 檔案

- `assets/template.pptx`：空白模板（0 頁，保留全部 42 個版型）。**一律從這份開始**。
- `assets/example.pptx`：原始範例簡報（6 頁），用來參考實際排版與文字密度。
- `references/layouts.txt`：每個版型的 placeholder idx、類型、位置（cm）。
- `scripts/build_deck.py`：JSON 大綱 → .pptx。
- `scripts/inspect_layouts.py`：重新列出版型（模板更新時用）。

## 流程

1. 理清內容：每頁一個主張。標準結構是 封面 → 內容頁 ×N → 感謝頁。
2. 為每頁挑版型（下表），寫成 `spec.json`（格式見 `build_deck.py` 開頭說明）。
3. `python3 scripts/build_deck.py spec.json out.pptx`
4. 轉圖檢查：`soffice --headless --convert-to pdf out.pptx && pdftoppm -r 50 -png out.pdf pg`，看文字是否溢出、圖片是否變形，再修正。

## 常用版型

| 別名 | 版型名稱 | 用途 | placeholder |
|---|---|---|---|
| `cover` | (一般內外部使用)封面 | 封面 | 0 主標題（可兩行）、10 副標題、16 報告人、18 日期 |
| `cover-blue` | （對外使用）封面_…_藍色 | 對外/高階主管封面 | 0 標題、16 副標、17 日期 |
| `toc` | 目錄 | 目錄 | 10 |
| `section` | （通用）過場頁 | 章節過場 | 10 章節名、11 說明、12 編號 |
| `content` | Content 2 | 標題 + 導言 + 一大區塊（條列或圖） | 0 標題、15 導言、2 內容 |
| `two-content` | Content 6 | 左右兩欄（如左圖右條列） | 0、15、16 右欄、17 左欄 |
| `dashboard` | Content 43 | 上兩區 + 下三欄（各有小標） | 0、15、2 上左、52/50 上右（上下兩塊）、47/49/51 下排左中右小標、46/48 下排左中內容（右欄常放圖） |
| `table` | 內頁（表格呈現） | 表格頁 | 見 layouts.txt |
| `thanks` | （通用）感謝頁 | 結尾 THANK YOU | 無 |

其他 Content_x 版型見 `references/layouts.txt`，直接用版型名稱。

## 寫作與排版規範（取自範例）

- **頁面標題**（idx 0）：一句完整主張，約 15–25 字，例如「整合語意分析、多模型架構與知識庫持久化儲存」。
- **導言**（idx 15）：一行粗體重點，模板會自動加橘紅色方塊。
- **內文**：用 `"## 段落標題"` 分組（範例用「系統邏輯」「使用工具」這類小標），每條以 `**關鍵詞**：說明` 開頭，一到兩行。
- 一頁最多約 8 條；超過就拆頁。
- 封面報告人格式：`報告人：<部門>_<姓名>`；日期格式 `YYYY.MM.DD`。
- 資料頁在頁尾（idx 3）標註 `資料日期：YYYY.MM.DD。`
- 圖片用 `{"image": "相對於 spec.json 的路徑"}`，會等比縮放置中於 placeholder。

## 色彩與字體

| 用途 | 色碼 |
|---|---|
| 深藍（副標、強調） | `#00377B` |
| 標題藍（封面主標） | `#2F5597` |
| 品牌藍（頂條、箭頭、表頭） | `#0065B2` |
| 橘紅（導言方塊） | `#E83F0A` |
| 橘（欄位底線） | `#D56C2A` |
| 灰（註解） | `#737373` |

字體：中文「微軟正黑體」、英數 Calibri（模板主題已設定，不需手動指定）。自繪圖表時沿用上表色票。

## 線上預覽版

同一套版型的 Claude Slides 範本（不含公司 Logo）：https://claude.ai/artifact/WUyssVjkAAUkgz4LQE8wQC
