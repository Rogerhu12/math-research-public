# 已付 p32 的完整 first-jet 标量入口：源审读与唯一执行范围

## 1. 本次新问题

原 cone32 已完成并封存：run 43800505444 / job 133079366251，source 8dfe5272b6d4f4fb752c8962689b22a95c61f78a。完整全步在 fine87417 分离后没有模型下降，所以没有物理 trial；它不能排除同一方向的内部尺度。原 32 cone / 64 HiGHS 上限不扩，旧 1200/1800 秒及 96/160 值范围也不改写。

本入口只做已发表[凸性证明](paid-p32-complete-grid-line-envelope-convexity-20261116.md)和[新方法设计](paid-p32-first-jet-line-envelope-method-design-20261116.md)的一个独立问题：恢复唯一已付 p32，在同一真实52、同一 g/b0/reference/159→163 坐标上，一次生成两张原完整网格的 e、f、de、df；使用一个有明确费用的有限标量搜索。若观察到模型下降，再让至多三个从未试过的点通过原实际几何/14门/精确163盒。

本稿是源文本审读；没有在本地运行研究、开发数组、符号或数值。通过、下降、接收与费用须消费唯一公开 Actions 原输出后分别发表。

## 2. 完整源闭包

root 已全文读六个新 Python 源、workflow、request 及三份已发表来源稿；最后 audit/report 只读源差异。request 的 200 个绑定准确为 176 Python、13 workflow、8 人读 Markdown、3 个历史 request JSON。原 cone32 的 189 个绑定逐项相同，原 98 个参数逐字相同。当前 request 不自我哈希；它在原 REQUEST stdout 中记录实际 bytes/SHA 与提交。

| 新源 | bytes | SHA256 |
|---|---:|---|
| frame_metric_p32_line_envelope.py | 34656 | 9b03e6c3d04e908778246c67b9d93baa05a19fe01712a99335cdcd8dcc6bfd07 |
| frame_metric_p32_line_development.py | 6461 | 99e9e3177c65bf524adf8b97833cbfce1dd1f9599d90b2b78dcfa97364d53e1c |
| frame_metric_p32_line_actual.py | 22034 | bbb827f59b26974487e0270b0b09af928f6e89c0bdfb79c7adb96b6a1149d023 |
| frame_metric_p32_line_transfer.py | 18532 | 777b6021a07ac3e12538db91f16ea707aeb7cf4c46415da5bbc7079504e2e452 |
| frame_metric_p32_line_audit.py | 24035 | 621e6eb2f772ad023e28edf4c78a3bb55c9f46a603172a400c5eb63fcbf02095 |
| frame_metric_p32_line_report.py | 19016 | 6f00bbff318c21891c3c7ac0f752e1f6a71e8aafacc856def1d364d88cc40cae |
| visible-p32-line-envelope.yml | 7048 | be5d9e0c095ee37a5ee234f3473eb34337f64b2e99bd899b319a8a9f56b2f38c |
| request-p32-line-envelope.json | 44738 | 7b300c90eeb4c4b7c1fefc5b449fd8c80ec8aa836b10324b2e34c9942d3936a4 |

最新三份来源的人读指纹同 published cone32、convexity 和最终16178B设计；没有用旧16015B设计、旧core或旧audit。来源 raw161、scale159、p159 的 binary64 精确字符串与两种明确命名的 digest 域分清。唯一原 log 的运行/作业/提交、四原 tag、189/170 闭包、真实52和全部原账在 runner 读取，不恢复更早 logs 或重做它们的研究。

## 3. 首 jet 公式及一次缓存

完整原 T、Ts 与原角向 Π 给 U；原 reference b 先加到 Uz，只有原五高度非零且位于原开支持时再加 Cq5。方向 dU 使用同一原 frame JVP 公式与 Cp5。e=U·U−1、f=U·T、de=2U·dU、df=T·dU+U·dT。原 Fourier 零模/Nyquist、物理径向节点、角节点、spectral epsilon=1e−8 和 target=13/50 均保。

此新对象只承诺 metric first jets。它不伪造含 X 的旧 ordinary/cache 身份，不启动 selected159 J、primary factory 或旧 solver，也不为只需 T/U 的模型先算位置冷前缀。固定 primitive 状态在本次 build 前后明确保留；如进入真实 trial，原完整 geometry 所需冷前缀及所有后续成本照实收费。

一次 build 直接将已完成网格数组放进外部 capture。正常完整 CACHE 在任何标量 query 之前作为一个原 plain JSON stdout 记录发出。若第二网格或总预算中断，唯一 partial CACHE 只保存实际已完成的网格；不重建、不以空对象覆盖、不再发第二个 CACHE。数组不编码、不拆块、不进 Git/artifact/Release/cache。

生产 adapter 只消费旧输出中已付的四个端点最大值、另四个全步最大值及四 attainer 的 e/f/de/df，共24比较。两端点 query 计入新64限额；未声称和不存在的旧全数组作逐位一致检查。旧6/12/11/9检查全部只引收据。

## 4. 明确的新费用和真实验收

新科学钟从 audit 启动且在输入前开始，包含 import、源码验证、新开发、原 log 读取、24输入恢复、系数构建、缓存序列化/输出、全部 queries 和真实 trials。独立总限600秒，其中新 development ≤30秒。新开发仅三个 scalar 数组用例，三个开发 session 与一个生产 scalar session 分开报告，旧用例不重做。

生产范围：1 build、2完整系数网格、1 scalar session、≤64完整包络 queries。主搜索最多62次（含端点及每次导数），保至多两次给实际半步/四分之一步的完整重查。所有数组最大值是原完整网格；浮点相等 active 和有限黄金分割不冒解析最优性或驻点证明。

最多三个实际未试尺度为 alpha*、alpha*/2、alpha*/4；每个先有本次完整模型下降高于原 floor，才进入原 full geometry。精确163盒、14门及原严格实际下降/合格 target 规则不放松。至多6个新两网 actual values，调用前 debit 与真正 geometry_started 分开报告；新 actual 行或容量变化使此固定线停止。actual pools 只按当前真实值缓存学习，绝不制造缺失 J/gamma/bank/growth 反馈。实际52的旧门直接引用；没有额外初值或末值 geometry。

祖先最终科学秒1324.8055252469999原样加上本次真实全部耗时；已含的 cone968.6757049859999另列而不再相加。祖先124 full values 加本次真正 started 数，32/64旧调用数永久闭合。所有非抢占调用实际超时照实记录，不裁成限额。

最后 P32_LINE_FINAL_CLOCK 在大 CACHE、COMPLETE、文件元数据序列化/输出之后采样；此前再查600秒。若最终输出期间越限，FINAL_CLOCK 的 scope_exhausted/status 覆盖较早 COMPLETE，不把已经接受的真实点抹去。COMPLETE 序列化失败也明确改错误状态，不能以无完整报告冒成功。

## 5. 为何新增这个 workflow

这次是新 first-jet/标量方法而非 cone33。完整 cache 预计超过原连接器整日志读取上限，根15又禁止上传研究 payload，因此在同一个 workflow 添加 needs:research、always 的只读 report job。它只使用标准库和原 reader，等待 research job completed，但不要求整个 run 已结束或 research success；只读一次原日志，输出全部关键费用、完整 trial159/163、cache原JSON+LF指纹和语义摘要。

report 不重新计算数组，不转发系数数组，不编码或拆分绕过读取限制；需要删重复 trial 视图时先与 native trials 逐项相同，缺 native 则保 COMPLETE 中的原向量。它的只读耗时独立于前一科学钟。partial / failure 也保原 cache 和已经发生的调用事实，不因此重跑 research。

两个 job 都先实际 public pull --rebase 并核根/题 README，只读差异；再私有 pull/核规则与唯一进行中 QUEUE。随后 detach 回本次精确源提交。rule 变更先停对应执行并由 root 处理新差异；MR_TOKEN 只环境内使用并在子进程前删除。没有 compile gate、旧 suite 或新增机械冻结。

唯一 request 随源码发布触发一次公开运行。结果无论通过或失败均只消费该次原输出，立即更新 HANDOFF/log/open 并接下一个尚未完成的研究问题；本课题整体完成门仍未满足。
