# R150：固定二十九条 Koszul 曲线的外一阶映射单射

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿关闭一个精确而有限的子问题：已付二十九条原多项式 Koszul 曲线作常系数线性组合时，除零组合以外，没有一条在原选列集之外消失到二阶。允许曲线系数依赖参数的校正仍未计算。

## 1. 固定原对象与待检映射

保持原 $6188$ 来源、$4367$ 输出、选列 $J$ 及其补集 $J^c$，其中 $|J|=4354$、$|J^c|=1834$。原自然参数为 $u=1/s$，原十七式分别按 $u^{10}L(1/u)$ 与 $u^5\Gamma(1/u)$ 展开。

令 $\Phi(u)$ 的列为固定 $1632$ 个标准 Koszul 关系：先按 $i<j$ 字典顺序，再按乘子 $1,m_0,\ldots,m_{10}$ 排序，列为
$$
m_\alpha\bigl(F_j(u)e_i-F_i(u)e_j\bigr).
$$
它们满足完整的原恒等式
$$
A^h(u)\Phi(u)=0.
$$

[已付精确支撑计算](R150-appendix-selected-koszul-curves-infinity-order43-and-source-cost8712.md)给整数系数矩阵 $X\in\mathbb Z^{1632\times29}$，满足
$$
(\Phi_0X)_{J^c}=0,\qquad
\operatorname{rank}_{\mathbb Q}(\Phi_0X)_J=29.
$$
这二十九个常项头已经用原三十六自由坐标逐项核验。

本次只新增
$$
M=(\Phi_1X)_{J^c}\in\mathbb Z^{1834\times29}.
\tag{1.1}
$$
对任意常向量 $c\in\mathbb Q^{29}$，
$$
(\Phi(u)Xc)_{J^c}=uMc+O(u^2).
$$
所以固定常系数组合的二阶支撑空间恰为 $\ker_{\mathbb Q}M$。

## 2. 真实原来源核验与完整秩

[执行源码](../notes/2026-11-15-r150-koszul-curve-first-outside-789f.py)先从原自然 $F_0,F_1$ 重构全部来源列，核验：

- $\Phi_0$ 的全部 $6188$ 行系数与已付标准族完全相同；
- 二十九条 $\Phi_0X$ 的完整原来源哈希、全部外部零坐标和原三十六自由坐标均相同；
- 新的 $\Phi_1X$ 在全部 $4367$ 输出上满足
$$
A_0\Phi_1X+A_1\Phi_0X=0.
\tag{2.1}
$$

全部 $1834\times29$ 整数矩阵在任何新有理消元前写入临时检查点。它有 $1239$ 个非零行、$8643$ 个非零条目，最大整数位长为 $2411$。只对这29列作精确有理 RREF，得到
$$
\boxed{\operatorname{rank}_{\mathbb Q}M=29,\qquad\ker_{\mathbb Q}M=0.}
\tag{2.2}
$$
完整核结果也写入临时检查点，并对全部1834行乘回。零维结果不能省略前面的满列秩检验；它不是把空乘回当成秩证据。

## 3. 对加权源因子的准确含义

[加权支撑阶引理](R150-appendix-weighted-support-orders-of-exact-kernel-curves-and-minor-gains.md)中，对这个固定常系数组合空间，
$$
t_2=29-\operatorname{rank}M=0.
$$
所以这一项探针没有提高先前已付的源因子：最大子式仍加29，低一阶来源因子仍加28。结合[完整无穷远43/39下界](R150-appendix-infinity-third-connection-one-dimensional-bound-order43-and-cost8663.md)，仍是同选 $72/71/67$ 和 $K_{80}$ 下的条件来源费8663。

若允许新增参数系数，则曲线可写为
$$
\Phi(u)\bigl(Xc+uY+\cdots\bigr),
$$
其外一阶条件变为
$$
Mc+(\Phi_0Y)_{J^c}=0.
\tag{3.1}
$$
(2.2) 没有证明 (3.1) 只能有 $c=0$。后者必须在原外常项像的商空间中检验，或提供具体 $Y$ 并完整乘回。也没有据此排除标准1632族以外的精确关系。当前关闭的只有固定二十九曲线的常系数组合子问题。

## 4. 实际执行与可恢复身份

实际 run **43679903558**，step **koszul-curve-first-outside**；执行源码提交 **9da4ca88ad22f148151a06f6288ec4918b2a8500**。数学时间 **2.028866967000795 秒**，墙钟 **2.1178155449997575 秒**，退出码0；限额30秒、512MiB。没有重做原1603秩消元、原常数秩消元或新增Dixon位。

| 对象 | 字节数 | SHA256 |
| --- | ---: | --- |
| 新外一阶矩阵 | 1726532 | 9d4b7650084b69d3158e101b86c150024794d12eb71e39d22eaff30ff726c0ed |
| 完整小核检查点 | 102654 | d9a4d27b699010ae473991a57616e853bf84a07ce34220ac2de9c36d9fc49d2a |
| 临时完整回执 | 14200 | 8ef23972406e280223bf953df25c374e7f089cece4b433906025c40f9ab8c28b |

源码 SHA256 为 d14abec1bdf614f2fa55ffd9a2e4d9c0155a4f93399328df932fa2132b6484a6；真实绑定为24e3518189b9e6654a795806f26a356087c22051cd2cf9a34ccc90f5a8f1bd10。[实际小记录](../notes/r150-infinity-remote-session-789f/43679903558-koszul-curve-first-outside.json)保全部输入身份与原乘回标志；可重算矩阵只在当前作业临时目录。
