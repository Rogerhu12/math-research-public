# R316：完整权零 self 成员成立，得到 pure 与全部 universal self 同时为零的正特征代表

日期：2026-11-15。**首次公开实际结果；未完成主课题。** 本文直接消费公开 [Actions 43735872441](https://github.com/Rogerhu12/math-research-public/actions/runs/43735872441)，job 132878270740，原计算源码提交为 [ca186db057ed753abe565d0c3c2c8305278b5af7](https://github.com/Rogerhu12/math-research-public/commit/ca186db057ed753abe565d0c3c2c8305278b5af7)。新接口人工与研究实际均成功，没有为形成本文重跑原科学或人工门。

## 1. 决定与准确原列编号

令 \(R_j\) **始终指 R126 的原 old-column 编号**，不是删列后的16列紧缩位置，也不是本次13列 pure 核的位置。其完整原响应定义由 [R234 输入接口](../scripts/literature_character_zero_endpoint_layer.py)、本次 [driver](../scripts/literature_weight_zero_complete_self.py) 的 zero.R0_KEEP 映射及五组冻结来源绑定共同确定。

R196/R201 的原目标为
\[
H=C_2+\frac1{48}R_0+\frac{11}{64}R_2-\frac{13}{96}R_3,
\qquad \pi H=0,\quad\lambda_+(H)=1.
\]

本次计算的13维比较空间是**全部**
\(R^{(0)}\cap\ker\pi\)，其完整 self 像秩为7；加入 H 后增广秩仍为7。37行是实际出现的 T/Euler 忠实坐标行，不把它们当作独立行。结果为 **MEMBER**。

具体取原 pure 核方向
\[
\begin{aligned}
K_4&=R_4-R_2+2R_3,\\
K_5&=R_5+\tfrac14R_3,\\
K_7&=R_7-\tfrac43R_0+\tfrac43R_3,\\
K_9&=R_9+6R_2-\tfrac83R_3.
\end{aligned}
\]
这些下标仍是各自非主元的 R126 old 标签。本次准确解为
\[
K=-\frac{649}{1536}K_4+\frac{821}{768}K_5
-\frac1{64}K_7-\frac{187}{1024}K_9,
\qquad \mathcal Q(K)=\mathcal Q(H).
\]
其全原列展开是
\[
K=\frac1{48}R_0-\frac{517}{768}R_2-\frac{343}{3072}R_3
-\frac{649}{1536}R_4+\frac{821}{768}R_5
-\frac1{64}R_7-\frac{187}{1024}R_9.
\]

因此一个明确的完整成本代表为
\[
\boxed{
H_*=
C_2+\frac{649}{768}R_2-\frac{73}{3072}R_3
+\frac{649}{1536}R_4-\frac{821}{768}R_5
+\frac1{64}R_7+\frac{187}{1024}R_9.
}
\tag{1}
\]
它满足
\[
\boxed{
H_*\in U^{(0)},\qquad
\pi H_*=0,\qquad
\mathcal Q(H_*)=0\text{ 对所有真实紧 profiles},\qquad
\lambda_+(H_*)=1.
}
\tag{2}
\]

这里完整 self 为 R314 的原右锚二次左尾泛函，不是一个固定母函数、平移族、偶函数或一个圆上的有限代入。

## 2. 为何这是整个比较核与整个 self

R196/R201 已支付 \(\dim R^{(0)}=16\)、\(\dim\pi R^{(0)}=3\)，原 pure 基列为0、2、3。本次只读48个已保存的三个 pure 查询值；其在这个已证明的三维 pure 像上忠实，未把三查询当作一般 universal 测试。

逐个非主元减去该基的准确 pure 投影，得到13个原 mixed 方向。每个有独特非主元系数1，故是整个13维 pure 核的基，包含这个权内的全部响应分支。未仅取 Z18 的某个方便子块，未重复原 R196 秩计算或原 pure 查询。

[R314](R314-ordered-matrix-defect-localization-and-faithful-Euler-self-coordinates.md) 的完整分解为
\[
q(V)=\mathcal N_{\mathbf T(V)}+\int L_V,\qquad
j_u=(u''{}^2,xu''{}^2,x^2u''{}^2+2u'{}^2).
\]
本次 helper 先将所有真实原积分中的两色全局识别，再执行完整同右锚 word 转换；保嵌套 primitive、左常数与全部三角对角项。九个有序矩阵项与局部密度的**整个六 jet 三次 Euler 多项式**共同给忠实坐标。

14个新目标均有原 whole-word 重构严格零，self 真权均为−2；九矩实际只有 T22 非零，符合 [R322](R322-full-self-scaling-shift-and-exact-reduction-to-the-matching-response-weight.md) 的准确权移，但代码先保全部九项而非预先删除其他项。原 H 的 T22 是1/1536；局部 Euler 余项也全部参加消元。秩7不是只算 T 或最高导数 principal 的结果。

R322 另外证明齐次 H 的跨全部真权响应支付等价于同权支付。本次正成员已有同权具体 K，因而无需计算其他权才能给(2)。本次没有求整个 U0 的 self 像，也没有恢复未需的 C4/C6 self。

## 3. 独立重建原复合差

为避免把消元数组上的相消当作原函数身份，driver 在成员解产生后，从原 mixed 根重新组成 H−K，创建一个新的 mapper，并对整个复合差再读 T/Euler 与 word 重构。

实际记录：

| 原对象或结论 | 原运行给定值 |
|---|---|
| 原 mixed 复合差项数 | 2497 |
| 原 mixed 复合差 SHA256 | c556d1a99522bb8cdc828d38ff00c8121ecaf7ad02dfe36861d26c547fb2ba76 |
| 全局对角表达 SHA256 | c181256a91943ff0df4474737cf097e91cfcf3851810bdeac62047da982df298 |
| 原 whole-word SHA256 | d5a7dda37c1e41c23680f1dda5d2599d94ba35e7346fecb3489e92904e07f679 |
| fresh T 与完整 Euler | 全部准确零 |
| whole-word 重构差 | 准确零 |
| 实际 self-word 项数 | 0 |
| self-word SHA256 | 4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945 |
| 原响应组合的三个保存 pure 坐标 | 0、0、0 |

最后一条 self-word 字面零是这次实际事实；一般成员判据只要求 R314 忠实 T/Euler 零与完整重构，不另要求某个非完备正规形字面零。公布的源码在首次实际前已按这点收窄判据。

因为 \(\lambda_+\) 在 R 上为零，原 R201 的 \(\lambda_+(H)=1\) 保留为 \(\lambda_+(H_*)=1\)。由(2)，在 \(U\cap\ker\pi\) 上，\(\lambda_+\) **不可能经过完整 universal self 线性因子化**：否则零 self 必被送到0，与1矛盾。这是具体代表的纸面推论；并非计算程序声称已经处理全部 U 的线性关系。

## 4. 执行、输入复用和预算

先执行12个全新接口人工：完整 Euler 的全导核/最高 jet；有序九矩及真第三矩；原积分内全局同色；嵌套原 J 增量与符号；三角对角项；未付双核与过长 word 明确拒绝；真权移；已知 pure 基到完整核；fresh 原复合差。12项全过，用时0.010078071秒，峰值28.28515625 MiB。旧科学根、profile 查询与旧开发套件没有在这一阶段执行。

研究实际完整完成14/14新 self 目标，用时10.428266294秒，峰值112.48828125 MiB。必要恢复为16个旧 mixed 原根与一个 C2 原静态根；48个旧 pure 值只读不重评。没有新增 N 响应、没有重编3974 forcing、没有重求旧 H0 全秩或旧17个 endpoint 目标。

完整 mapper 共413次新 primitive 调用，其中共享 mapper 220次、fresh复合193次；最大 word 长度2、cycle fallback0。literal monitor记录677次操作与40位最大整数，这个 monitor **不是整个表达 DAG 的全部算术总量**。

原请求上限为240秒、1024 MiB、8192位有理数、100000项、300000次 primitive、250000缓存项；实际没有因预算截断。

## 5. 可追溯来源与只存元数据

原运行回执为 [receipt](../notes/actions-43735872441-1-weight_zero_complete_self/receipt.json)，本次请求有33个源码绑定：30个科学源码加 workflow/publisher/printer。原研究报告的45个嵌套源码记录（含重复依赖）与回执文件 SHA/字节逐项核对；请求33项亦与回执一致。哈希只承担来源绑定，成员结论来自第1至3节的实际准确计算。

| 项目 | SHA256 |
|---|---|
| 本次 driver | 9347caeb4ff7ed54cc88f6c38183d4773d8e12125a5a9631412674550d42b78f |
| 完整 self helper | 95ec818ce1fdf815b0390aaf2ad4f976a0dfc7bd0b5218899acd4f4bc271f9ba |
| request | 15068701ad99510e759211d2700b29edf4d845115c5f911efd27e334ae98d0c9 |
| 人工输出，9926字节 | 7f4727989a54105877c995d3a1a54b59ce13aa6789702f32f6b43dd30e8f9388 |
| 实际完整摘要，61441字节 | 731ffae43cc8f06346801c444a7de010fe2cf6f9f05ecf4b650d319fa2ee06fd |
| 内存证书，95310字节 | 0e736737731f3060943bd5a974a29c48cf0d258bb79689ba127e6e11b5fb604b |

两份 COMPLETE_REPORT 原日志 JSON 加换行的字节与上述两份输出 SHA准确一致。证书未写入仓库、Release或artifact；可重算数组不随本文存档。原运行还实际pull公开 main到 c818ac3f4c9b1a0ab3c9fc674fa2d6770548e18d，并核双README无差；私有16:31:15实际pull到 dc99543da830ee95eadc86a5fd30af7b45a10b48，规则无差、QUEUE本会话唯一进行中。

## 6. 新边界与立即继续的工作

(2)关闭了“正 \(\lambda_+\) 代表必有完整 universal self 障碍”这一可能推断。它没有把一条线性空间响应组合变成实际有符号控制，也没有证明完整成本函数 \(H_*(f,g)\) 对任意不同 f、g 都为零。相同 profile 的四次对角泛函为零，不可直接删除外槽/内槽不同的混合观测和真实历史。

下一步沿 R302 的共享原型、真实倒行、完整 history 和几何增强IFT，研究(1)的真实可实现性以及完整 mixed/cross 门；同一 w 的 period/ruling 相容仍须原式联立。R304/R306已排的旧圈族不会因(2)自动恢复。新端芽 R312/315/318/321 的局部门也独立继续。

目前无满足 README 全部条件的完整曲面候选：固定 g 的有限 C² 等距族、全时嵌入/reach、幅度及精化门均未付全。继续 open.md 的未解问题，不以本次成员结果结束。
