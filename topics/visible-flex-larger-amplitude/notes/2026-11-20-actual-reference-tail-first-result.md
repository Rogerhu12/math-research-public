# R671 新解析尾：同固定 g 的首个完整方向实际返回

本条仅登记[公开run44758209061/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44758209061)阶段30真实返回，实际控制器记录见[第1卷](2026-11-20-public-actions-44758209061-1-part-001.md)。它不是旧44748103105中出版故障丢失的R671结果，也不拿那个未留证据的返回值补本条。

## 输入、执行与完整模型

本job必要输入再生返回同一个实际父bundle `c4a3f010691c8e9d1a1d9a8b26bfe4bc9b136efecf8fc3a9426ecddf28289080`，不是仅凭预定历史SHA选父。其本次coarse report SHA为 `2e6c4a8bca3fd189156a98f864e539a8527d1da903143562b2344fdc9c769ce1`，实际末阻尼 `0.0007539530259341321`。完整位置原清单119473B，纯空白压缩后60538B、SHA `cb095d37b0c2b3d5f0d81b8ddc88e314fddf3448e34f64fc3c16eb954c7cfd44`；1635曲率点、244半径点、19保护点及全部键/顺序均保持。来源路径随job变化，清单SHA不冒成旧run的SHA。

实际source commit `cc0fb52718e158ed3c7f97d69048e938c50ea3d0`；入口 `launch_full_phi_exact_tail_from_coarse.py` SHA `0b24107f041ae1eece4958c4f22ef646597f8f365c06e2617d10502609f1749c`，完整driver `b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8`，factory `2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216`。保全部原未知量、7377径向行/完整2048角及quarter重数、原同a/正谱Phi/physical H2型步范数和全部永久点。

实际外层参数为：lambda=1、source-lambda=0、eta-start-node=885、migration=nodal-projection、directions=1、maxiter=256、active-rows=192、reach-safety-factor=.992、active-band=.025。完整绝对argv及各输入路径在实际卷中，固定版本源码完整保留；不重新手写一套不同命令。此次迁移不是场恒等，初场须按新模型真实读取；只有它通过真实必要点筛选之后才运行QP。

## 实际初场与接受终态

| 有限量 | 新尾初始化 | 真接受终态 |
|---|---:|---:|
| normalized Phi | 1.1231363492447929e-7 | 9.526119203703808e-8 |
| 最大 relative Gram 谱范数 | .013196553081925468 | .012594260006200009 |
| 原weighted SSE | .19536076269227826 | .19157178903063204 |
| 已知点 necessary reach product | .9919039369253358 | .991950785480054 |
| 原.992必要点筛选 | true | true |

一个完整方向自然返回；真实接受alpha=.5。入口共681.4890348849999s，方向记录665.5079870990003s，实际进程峰1947764KiB。终态sample_target=false。初场Phi与旧表示的c4a3略有变化；本表真实相减的前后是本次新模型自己的初场和试步，不把迁移当成准确同场。

QP为256次Hessian推进、status=iteration_limit。初gradient norm `8.323577678148328e-6`，实际gradient tolerance `9.323577678148328e-12`，末活动面projected gradient `6.09099396435621e-7`，最大线性违差 `7.030373462210693e-20`。报告最小原始乘子 `-3.5832005600113055e-6`；原始乘子不等于R668标准化释放率，不能据它或末gradient单独宣布约束QP驻点、全局最优或数值瓶颈。该批真实接受半步，依冻结更新规则末mu仍为本批mu；后继入口会从完整report重放，不硬抄这个数。

## 实际输出身份

| 输出 | SHA256 |
|---|---|
| final.npz，10381410B | `97fdc9ea3af7c24720db940b41a1d783894648984411fbf4aaf026259c3a8dcc` |
| 完整report.json，5535722B | `11a9e03f39b2850f40848167a371c08e69f67bf3a6b500b793019f08dbe78dcc` |
| exact-tail-lift-profiles.npz，150840B | `37c952dac200c6569a8c7a39be1212f465001c112b441ebd087be94e272da78d` |
| profile说明，11271B | `64568808181901c2e02efe691eff7d353cfcaa91ed00b5f8bd59261fc73af39a` |
| 完整from-coarse命令说明，19014B | `438d01b2dd86b376003d29d6c4f52647692c62b90efe59380e2d5d050d05ecf4` |

canonical model SHA为 `b6adb4df6dbd85d6a940b45af44225adf18212e3dfc7f5744aa03144be04341a`。全部raw仅runner。只有自然退出后，控制器删除本次新生成的2051701248B不等式行cache；未删除父、输出、方向或永久位置。全部声明输出存在。

唯一summary_errors是正常未停止时不存在的 `stopped_before_linear_iteration` 字段；它不表示科学子进程失败，也不补成一个虚构的停止原因。实际初场筛选和方向已经返回，区别清楚。

## 已付范围与立即续作

本条支付新R671完整模型的一次真实可行初始化和下降接受；不支付连续metric≤1e-6、全域K/reach、同场全t嵌入或固定g精化收敛。原同父.992旧表示pair也接受半步，但两种完整表示的方向不同，本条不把细小数值差解释为单一机制的因果优势。

同job已排该真实report的纯JSON瓶颈消费、新场f122全域首几何及b36非平面消费；原模型完整六方向和固定g径向精化继续。非零模型后继入口已完整保存，只允许同lambda/准确eta、真实末mu和全部永久位置的keep-q续算。后续证书必须绑定本条97fd实际新场及其canonical model，不能继承原c4a3或旧pair的数值。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
