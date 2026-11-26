# 圆核入口的真实启动失败与最小角网格修复

2026-11-26。原run [45775603393](https://github.com/Rogerhu12/math-research-public/actions/runs/45775603393)，job [139758402600](https://github.com/Rogerhu12/math-research-public/actions/runs/45775603393/job/139758402600)，source `a925b21604feed5fd578c5878d09514a040e1883`。该job自然failure后读取完整原stdout，未读取过在途日志。

原request SHA-256 `fe561a6e7a1c2a11586e99a5583d653a2f7c0bfa0f892d2a4310418de8ac52d9`，3952字节；圆核脚本SHA-256 `7e2032a6dd4e21f17c02aa4c77251357c6b57a325fcae689ac3b9b83fd3e64f2`。原decoded stdout为134144 UTF-8字节，SHA-256 `168286ebcbeb978f94d47f8ae12be1854581183e3e948ffda477ae77c8bc7b6c`。原log只留scratch供独立核验，不入Git或云blob。

## 失败发生在科学几何构造之前

固定mode=4，而request给圆核初始角节点16。底层v2 `Model.__init__` 的既有保护条件是 `theta_nodes >= 4*modes+4`，本例至少20。圆核入口自己的浅层CLI检查只要求4的倍数，没同步这一实际下界。

因此第一次 `Model(par,nodes,16)` 立即在v2构造器保护处抛出 `ValueError: positive resolved radial grid and an even angular grid required`。尚未进入核心弧长求解、角/径向基生成、尾height积分、几何扫描或SLSQP；没有`CIRCLE_CONTINUATION_DEFINITION`、阶段、回调或FINAL科学收据。不能从执行failure推导圆核几何不可行，也没有任何已完成科学优化可重复或恢复。

child由07:29:05.999002 UTC开始，到07:29:06.603801 UTC以returncode1结束，入口wall耗时.604799秒。该wall包含解释器导入/参数入口，未另输出科学模型耗时；不把它伪写成免费成功计算。

执行前真实public pull从source到 `f4fccfb2c8ec1e18744cb71030b7dbd34ead316d`，根README和课题README差异均空，blob分别仍是 `282e86b03385d3b6245ce7100ae2e2af7b103c2d` 和 `d0432faff569c8e9af7ed4809847e12880976c11`。真实private clone/pull到 `25305b1bed54c40cbb444175cfdd03e011e8f9cd`，根blob `5ba164843b1f5802184178a82d786264404873a3` 一致，QUEUE核对本会话进行中且唯一。固定Python/NumPy/SciPy运行环境正常，凭据已在child前移除。

## 修复身份

新源码schema为 `inverse-r566-circular-core-radial-entry-and-design-continuation-v2-resolved-circle-grid`。圆核默认/请求角约束改为32，fine64；圆核与后继两处CLI角网格都要求达到真实 `4*modes+4` 下界且为4的倍数。底层受保护的物理模型不改，原17变量圆核输入、p续接策略及所有几何门不变。

新request明确携带这次启动失败的source/run/job/原request哈希。再次执行才会首次真正重建这一圆核输入；不重做任何已完成的几何或优化。仍只有本地AST/源码身份核验，科学模型继续只在新的公开Actions执行。原16/fine32配置的实施说明是历史记录，本修复记录准确覆盖新32/fine64配置；不回改原run身份。
