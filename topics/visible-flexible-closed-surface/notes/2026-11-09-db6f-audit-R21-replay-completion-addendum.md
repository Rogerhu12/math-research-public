# R21 独审补记：完整 M12 尾 metric 独立重放已完成

本补记只补齐 `2026-11-09-db6f-audit-m12-whole-and-decrease.md` 当时明确保留的一项运行证据；原审稿、原证明和原数值证书字节不改。本审查者未参与该 M12 前缀／尾部非线性求解优化。

root 的独立后端运行已经真实退出 0。其完成记录为 `2026-11-09-db6f-root-review-m12-full-metric-replay.json`，SHA256 为 `73f3678feb51c2d61ea3378c751311d0b2926ae68cc223ea974575daaa702fae`。本审查者另行读取两个原始完整报告、两个压缩全行文件和该完成记录，运行新脚本 `scripts/db6f-audit-full-metric-replay-completion.py`，实际退出 0。新检查输出为同日期前缀的 `db6f-audit-full-metric-replay-completion.json`。

检查结果：全部 30,971 行逐字段相等；两个全行 gzip 文件的 SHA256 均为 `06706fee1a59c4f0ce15ebde39af24e323bd077cf1819020ab660c8221c41f7d`。全域覆盖标志、collar 标志、输入 manifest／packet／data／source 哈希以及所有数学字段完全相同。两个总报告实际只有运行时间、峰值内存和全行文件名三个字段不同，本检查没有排除其他输入字段。逐行最大值与总报告一致，其严格上界仍按原 binary 端点解释为

$$
\varepsilon_{\rm tail}
=\frac{7055251261315967}{302231454903657293676544}
<2.334387\times10^{-8}.
$$

本次只检查已经完成的重放文件及全部结果行，没有再做第三次后端运行。这补齐了 R21 草稿首部当时保留的完整独立 metric 重放；不改变既有实际曲率证书、不扩大新 metric-only 后端的作用域。原 R21 独审的同一个 $g$、闭合两 jet、全时作用、含反射的非全等性、实际误差严格下降以及所有保留限制仍按原审稿成立。

**G5 仍未支付。** 本补记也不是最终另请一位未参与构造人员完成的统一端到端验收。

复现命令（输出使用新路径即可）：

```sh
python scripts/db6f-audit-full-metric-replay-completion.py \
  --out notes/2026-11-09-db6f-audit-full-metric-replay-completion.json
```
