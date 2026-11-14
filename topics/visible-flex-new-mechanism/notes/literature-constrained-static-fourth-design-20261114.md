# R114 受约束静态局部商 consumer：消费既有导出并修复完整报告保存

日期：2026-11-14。**实现设计；新源码尚未执行 Python。** 没有本地编译研究目标。新源码先在本公开仓库 Actions 运行语法及人工检查，再运行有界目标。

## 1. 本轮解决的具体问题

首轮公开 run 43645177423 已保存 W 和完整静态局部密度原式。它支付 profile 仿射权 $+2$；$+1$ 留下乘 $hk$、$hk^3$ 的两个改写余项。它没有证明这两个函数非成员。最后主报告超 95 KB，旧接口只保 hash/fallback；完整原式导出和两个已完成块不受影响。

[R114](../results/R114-constrained-static-costs-and-real-zero-matrix-words.md) 证明，正配平常态成本全零的准确条件为

$$
[\ell_0(S)]=G(m_0(S))
$$

而不是每个原几何系数分别属于 $\mathcal R_8$。新 consumer 直接计算

$$
\ell_{\rm norm}(S)
=\ell_0(S)-\sum_{i=1}^8a_i(S)\ell_0(S_i^*),
\qquad
m_0(S)=\sum_i a_i(S)m_0(S_i^*).
$$

八个有理状态取 $h=1$、$d=0,1,-1,2$，每组 $k=0,1$，$\omega=d+k$。参考矩阵由 R73 的已证点态公式准确计算，8×8 有理逆与 Kronecker 条件均核；没有对实际几何或 profile 做采样。

默认只消费 **profile 权 +1**。先取权再做这个几何线性归一化；二者交换。旧未约束的 +1 目标不重跑，+2 也不重跑。若新块有余，仍只报 identity_not_found，不把不完备改写当成真非成员或实际成本。

## 2. 源码与身份

新文件：

scripts/literature_constrained_static_fourth.py

24202 bytes；SHA256：

814e1338679914b32542f8b360978281002ee02a2c4e8c03912aa40c876786f4

未挂 blob：

018fe087fe87696291a3e45b93db5ca3b4d41b8b

旧 producer literature_local_fourth_quotient.py 保持 9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0；没有改写已发布导出的来源。新脚本复用旧 load_export/decoder，核全部原根 hash、同一 W36 和所有语义依赖。

publication helper 只调用 literature_full_m8_tail_response_projection.verify_publication_binding，绑定修正后的整件 SHA：

e66bf0d2f41570526d5e6b05aedc28118a18a492a299e097d341cc71e804e345。

它不调用该脚本的实际 m8 投影、模板恢复或人工入口。该纯输入 helper 已在前一公开 job 通过人工检查；其后修订仅修复尾 consumer 自己的 v2 字段读取，新脚本显式绑定最终整件身份。

## 3. 原始输入完全固定

默认目录为：

notes/actions-43645177423-1-local_fourth_quotient/

源 run 43645177423，源提交 2f1b809c0b0abb7a26303d36940edc203815f872。

- 主 report：local-fourth-quotient.json，3982 bytes，SHA256 19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a。
- 真实终端 publisher receipt：receipt.json，SHA256 c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba。
- 完整原式：local-fourth-quotient-original-expressions.json.gz，657195 bytes，SHA256 ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace。
- 解压数据：3518194 bytes，SHA256 d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1。

旧 fallback 缺 source/run 字段，新入口从真实 publisher receipt 核 repository、lane、source/run、原 producer 字节与 main/export packed/raw 身份；不是在旧报告中补造字段。所有显式 SHA 均可通过 CLI 换源，但源码身份发生变化时仍须显式重新绑定。

输入 gzip 只在 Actions 的文件系统读取；不通过 API 读取二进制或切块数据。W、lower fields、local density、旧第四 forcing 的编译入口均不调用。

## 4. 准确代数与正反结论

对每个请求权，入口：

1. 从旧原式按真实 profile 仿射整权投影。
2. 在八个有理常态取局部几何系数值。
3. 用固定矩阵逆构造八个 $a_i(S)$，从原式形成 $\ell_{\rm norm}$。
4. 逐参考态检查归一化后的原式准确为零。
5. 对完整两模式 $-4,-2$ 使用同一组实 R8 列；复用已发表 forcing-free 响应接口。
6. 丢掉的响应依赖及所有正面成员身份都从原始 W 模板重新组成，核原式差为零。

只显示代表秩时，把它记作真实响应维数上界；未额外证明独立性。非零代表余项不授真实非成员，更不授 $\mathcal U_4/\mathcal R_8\ne0$。R114 只有在实际函数层证明受约束门失败时，才把某个正配平成本变成充分大有限圈的真实非零成本。

默认 $+1$ 即使全付，也只支付静态部分的这一 profile 权。其他 profile 权、几何导数权 $2,4$、完整受约束积分、第四 ruling 以及有限等距族仍欠。

## 5. 报告体积修复

新主报告始终包含真实当前 source/run/repository、实际 completion、原输入绑定、完成块、耗时/内存、完整报告的 packed/raw bytes 与 SHA。原摘要超上限时，不再丢掉 source/run 或用一个格式 fallback 吞掉已完成诊断。

完整报告总是先保存为：

constrained-static-fourth-complete-report.json.gz

主报告为：

constrained-static-fourth.json

完成块也先保存 gzip；当原 JSON 小于主报告上限时另保可直接读取的小 JSON。例如：

constrained-static-fourth-weight-+1.json.gz

constrained-static-fourth-weight-+1.json

每个 gzip 与全输出仍有硬体积检查。若完整压缩报告真超过预算，会明确 report output_limit，同时保实际计算 completion；不会冒称已持久化。输入的旧大导出不复制到新输出目录。

默认资源：180 秒，RSS 软轮询 1024 MiB，400000 coefficient nodes、100000 atoms、150000 terms、1000000 rewrite calls，消元有理位长 8192；主报告 90000 bytes，完整报告或块 gzip 单件上限 2.5 MB，总输出上限 4.8 MB。

## 6. 人工门与实际 CLI

小人工门只处理：

- R114 的固定 8×8 有理矩阵与 Kronecker 条件；
- 人工密度 $\sum_jm_j(S)x^jq^4$ 的归一化严格为零；
- 人工密度 $hk^3q^4$ 的余项准确为 $h(k^3-k)q^4$；
- 大人工诊断完整压缩往返，核小主报告保 source/run/completion。

这不是旧真实 $\ell_0$ 的计算。当前尚未执行本次新 Python 源码；公开 job 应顺序运行以下三条。

第一条：

python -m py_compile topics/visible-flex-new-mechanism/scripts/literature_constrained_static_fourth.py

第二条：

python topics/visible-flex-new-mechanism/scripts/literature_constrained_static_fourth.py --toy-only --output /tmp/constrained-static-development.json

第三条：

python topics/visible-flex-new-mechanism/scripts/literature_constrained_static_fourth.py --weights 1 --max-seconds 180 --memory-mib 1024 --output /tmp/constrained-static-fourth.json

人工门通过后才继续实际。所有 source/publication/default input 均已明确，没有新的候选搜索或长几何优化。
