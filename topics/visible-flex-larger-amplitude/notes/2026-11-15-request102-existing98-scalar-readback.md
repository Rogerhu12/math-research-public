# 请求102：读取已有实际98的原始标量结论

**类别：读取接口；未新增科学计算，也未预填读回结果。**

原计算为公开 [run43677587785](https://github.com/Rogerhu12/math-research-public/actions/runs/43677587785)，source `918fdb11dbb7a424b6149b405e2c7fab3cc0c737`、job132701028492。模型、完整原FD和artifact生成已成功；旧发布步骤因README变更停止。原日志明确给α=0.25接受、同模型merit43.42621386634224→43.36604610143146、actual_model_slope=-0.24800196273797923、actual/model ratio=1.0029891422465396，原FD pass/maxrelative8.408533903133078e-10。尚未用日志替代原31查询的域、完整RMS/BC、拒绝原因或全部最终标志。

## 明确输入和范围

脚本 `computations/root_20261115_read_existing98_scalar_summary.py`（SHA256 `7e5f36100ffafe1ffe44cc878e18aeb2af3c4c73fcce7f64f21a22ec9313a083`）只在公开Actions读取原artifact14147700690，名称 `visible-followup-condensedqp-43677587785-1`，809042943B，ZIP SHA256 `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`。原byte-only transport51224788保持。

原request与workflow从上述source的GitHub API临时取得，Git blob分别为6aa7cc61e52b314c31699e8849fb9a9cc5c11b62和f998c08cc5320559204b7b2d5a67f4f2f1afdc99。完整ZIP大小与SHA通过后，仅解压五主要文件：model-000、driver-status、condensed-QP-summary、response-check、warm-001。每个实际文件保原字节/decoded SHA；warm须符合原job日志b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67。

摘要复制原JSON中的标量、有限查询、完整trial顺序、原接受/失败/最终标志和来源元数据；大数组或长历史树只列省略范围及原文件hash。没有重新评价RHS/J/ODE、求FD或优化，没有重新分类科学接受，也不声称未读数组已审计。超过90000B就明确失败并报告长度/SHA，不能静默截去某个trial。

## 运行与保留方式

新workflow `.github/workflows/visible-larger-public-existing98-summary.yml`（SHA256 `15dc24ee7189904b7ea6d1bce92b5ee58a0e052b3d10e401f29ec6edd8e929e7`）由短request触发，只有contents/actions read权限。先核两README和两源SHA、在Actions做AST；终端不可用，未宣称本地AST或真实git pull完成。所有原payload位于runner临时目录，成功摘要前删除。日志标记为 `BEGIN_ACTUAL98_SCALAR_SUMMARY`、`END_ACTUAL98_SCALAR_SUMMARY`，之后输出原摘要字节数/SHA和retained0。

根README137c5a的新第15条取消旧Release方案；此流程没有artifact、Release或Git原数据发布。读到实际结果后保存紧凑正式结论和下一步参数，继续构造。上述读回身份只用于防止引用错轮输出，不增添科学接受门，不阻挡其他计算线路。
