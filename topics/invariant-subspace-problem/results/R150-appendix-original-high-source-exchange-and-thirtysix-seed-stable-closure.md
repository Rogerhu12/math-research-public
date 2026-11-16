# 原十四高权来源的完整交换与三十六低权种子的同一稳定闭包

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

## 1. 已完成的两项不同结论

保持原合法有限域剩余映射 $(p,d)=(127,100)$、全部十二参数、十个模坐标和十八个原生成元来源。本次消费已付完整权八矩阵的七十四条真实关系，实际完成：

1. 十四个旧高权来源的坐标投影秩恰 14，且十四条替换式全部通过原十坐标和十八生成元乘回。普通参数 $B$ 模的命名生成元数仍是 **106 换成 106**；
2. 同一个原临界商的最小共同 $N_i$ 稳定闭包，可以从 **36 条低权原种子**出发，且其完整第一轮乘法扩张就是上述已付 106 生成元参数模。

这两项不能混同。第二项不是普通 $B$ 模由 36 列生成的断言，也没有证明第一轮已经稳定、单位理想、特征零成员性或某个数值停止阶。

## 2. 原字典与已经完成的完整关系

取

$$B=\mathbb F_{127}[y_0,\ldots,y_5,w_0,\ldots,w_5],
\qquad b=y\cdot w,$$

$$F=B^{10},\qquad \operatorname{wt}(y)=1,\quad\operatorname{wt}(w)=2,
\quad \operatorname{wt}(F)=(0,2^5,4^4).$$

同一原五个参数矩阵是 $N_i$。六条均值 $Y_j$ 权五，二十条保留交换子 $C_\ell$ 权六，十四条保留交换子 $D_\ell$ 权八。记

$$V_{ij}=N_iY_j,\qquad W_{i\ell}=N_iC_\ell.$$

[完整权八前沿](R150-appendix-original-complete-weight-eight-frontier-rank1312-and-twentysix-new-sources.md) 已付全部 $17674\times1386$ 原矩阵秩 1312。其前 1286 列独立，具体为完整 $G_8$ 的 1106 列以及全部 180 条 $y_aV_{ij}$；最后一百条 $W_{i\ell}$ 保留 26 条、删除 74 条。

这七十四条关系的目标单位坐标各不相同。因此它们恰为此固定权八映射的完整常数核基，不只是某个来源子族的关系。

原十四个 $D$ 在完整输入字典中的位置为 1092 至 1105，且乘子均为常数 1。程序逐原标签和乘子检查此范围，没有从新正常形坐标猜测旧来源编号。

## 3. 真正的 $74\times14$ 投影与原换源

将完整七十四条原关系投影到十四个 $D$ 坐标，得到一个小矩阵。本次实际消元给

$$\operatorname{rank}_{\mathbb F_{127}}\bigl(K|_D\bigr)=14.$$

小消元同步保留原七十四条关系的全部常数系数组合，并对十四条主元关系逐全部 1386 坐标乘回，实际通过 $14\cdot1386=19404$ 项检查。主元 $D$ 坐标块为 $I_{14}$，其它被删 $D$ 坐标为零。

这十四条主元关系只使用所选十四条实际依赖式。由于每条原依赖式只含它自己的新目标和旧独立输入，它们涉及的新目标仅是：原已保留的二十六条 $W$，加上本次选出的十四条先前删除的 $W$。

令 $K$ 为原二十六条保留像的索引，$J$ 为本次十四条补回像的索引；二者不交。本次每条 $D$ 的准确表达式都只使用

$$Y_j,\ C_\ell,\ V_{ij},\ W_{i\ell}\ ((i,\ell)\in K\cup J).$$

所有系数是完整参数多项式，只对固定有限域常数取逆，不倒置 $y,w,b$ 或任何参数子式。

程序逐式核全部十个参数坐标，并对同一组合的十八原来源核完整多项式乘回。若原十单项式向量为 $m$、原十八生成元列为 $A$，每条已付列 $v$ 满足 $m^{\mathsf T}v=A^{\mathsf T}\sigma(v)$；新 $D$ 来源取同一参数组合的 $\sigma(v)$。它与原 $D$ 来源可以相差真实原 syzygy，但两者均给同一原目标，不能要求来源系数本身逐项相同。

## 4. 普通 $B$ 模的 106 换 106

定义

$$\mathcal L_{50}=B\langle Y,C,D,(b-1)e_a\rangle,$$

$$\mathcal P=\mathcal L_{50}
+\sum_{i,j}BV_{ij}+\sum_{(i,\ell)\in K}BW_{i\ell}.$$

它的命名生成元数为 $50+30+26=106$。已付七十四条来源给

$$\mathcal P=\mathcal L_{50}+B\langle V,W_{\rm all}\rangle.$$

现在用本次十四条完整替换式，定义

$$\mathcal P'
=B\langle Y,C,(b-1)e_a,V,W_{K\cup J}\rangle.$$

其命名生成元数为

$$6+20+10+30+(26+14)=106.$$

两个包含都由真实来源支付：

- 每个补回的 $W_J$ 已由父完整关系表示在 $\mathcal P$ 中，所以 $\mathcal P'\subset\mathcal P$；
- 每个删去的 $D$ 已由本次完整原乘回表示在 $\mathcal P'$ 中，其它原 106 生成元都保留，所以 $\mathcal P\subset\mathcal P'$。

因此

$$\boxed{\mathcal P'=\mathcal P.}$$

本次统计的是十四条实际被换向量的参数单项式数：旧 245530 项，新 245458 项，只减少 72 项。不能据此宣称普通模大幅稀疏化或后继标准基必然更快。该统计也不是来源系数项数的统计。

## 5. 三十六条低权种子的最小稳定闭包完全相同

令

$$\mathcal L_{36}=B\langle Y,C,(b-1)e_a\rangle.$$

其中只有 26 条非 Bell 列，权分别为五和六；其余十条是原 Bell 列。对任意 $B$ 子模 $L\subset F$，记

$$\operatorname{Cl}_N(L)
=\bigcup_{r\ge0}L^{(r)},\qquad
L^{(0)}=L,\quad L^{(r+1)}=L^{(r)}+\sum_iN_iL^{(r)}.$$

这是包含 $L$ 的最小共同 $N_i$ 稳定子模。因为 $N_i$ 是 $B$ 线性的，原 Bell 子模自动稳定：

$$N_i((b-1)e_a)=(b-1)N_ie_a\in(b-1)F.$$

本次实际付出的十四个 $D$ 表达式只用 $Y,C,N_iY,N_iC$。故

$$\mathcal L_{50}\subset\mathcal L_{36}^{(1)}
\subset\operatorname{Cl}_N(\mathcal L_{36}).$$

另一方面 $\mathcal L_{36}\subset\mathcal L_{50}$，所以单调性给

$$\operatorname{Cl}_N(\mathcal L_{36})
\subset\operatorname{Cl}_N(\mathcal L_{50}).$$

由 $\mathcal L_{50}\subset\operatorname{Cl}_N(\mathcal L_{36})$ 及 $\operatorname{Cl}_N(\mathcal L_{36})$ 的稳定性，再得反方向包含。于是

$$\boxed{
\operatorname{Cl}_N(\mathcal L_{36})
=\operatorname{Cl}_N(\mathcal L_{50}).
}$$

旧原 116 种子的普通参数模已等于 $\mathcal L_{50}$，所以这也是原 116 种子的同一最小稳定闭包。

结合 [原十生成元与全部 116 来源](R150-appendix-actual-original-ten-generator-parameter-module-and-116-certified-seeds127.md) 的完整 border、字面 cyclic 路径和原十一矩方程门，以及 [稳定闭包的完整双向论证](R150-appendix-original-nine-generator-parameter-module-and-certified-stable-closure.md) 的同一十行版本，得到

$$\boxed{
B^{10}/\operatorname{Cl}_N(\mathcal L_{36})
\simeq B[u_0,\ldots,u_4]/(\partial R',b-1).
}$$

这是同一个原 Bell 临界商的有限域表示，没有遗漏 rank3 或 rank4 参数分支。

## 6. 完整第一轮已经付清，稳定停止仍未付

三十六种子的全部 $N_i$ 像由三类组成：

- $N_iY_j$：全部 30 条已付；
- $N_iC_\ell$：全部 100 条已付；
- 原 Bell 列的像：已在 Bell 子模中，有上节字面表达。

因此其完整第一轮恰为

$$\mathcal L_{36}^{(1)}
=\mathcal L_{36}+B\langle V,W_{\rm all}\rangle.$$

本次 $D$ 替换及父七十四关系给

$$\boxed{\mathcal L_{36}^{(1)}=\mathcal P'=\mathcal P.}$$

这不仅是“某些首层来源”的声明：三十六种子的全部五算子像都已覆盖，得到完整第一轮的 106 列普通参数模表示。但不能从这里推出 $N_i\mathcal P\subset\mathcal P$；第二轮仍可能产生新来源。十个坐标也不提供十轮稳定的上界。

后继正证可在任何实际有限前缀中构造 $e_0$，并按

$$\sigma(N_iv)=u_i\sigma(v)-S_iv$$

持续回填原十八来源。有限域正证仍须在原数域 $E$ 中恢复并核全部原乘积，才能支付特征零 Bell 自然幂。本文没有这样的新增单位来源或自然幂指数。

## 7. 实际执行身份

本次没有重做 17674 行消元，只读实际父完整矩阵、字典、native 结果及原来源阶段。主源为

~~~text
notes/2026-11-16-r150-weight8-old-high-source-exchange127-789f.py
blob b274ce3eeb5698ae3abb84322c72a1941fea48b1
13777 bytes
SHA256 b3e358f5da42777eedbaaea0a7715c754e22f7cc705d3c9f3e5714570355a803
~~~

两次执行均使用 Python 3.12.14、python-flint 0.9.0、768 MiB 上限。完整 CLI 和所有输入 SHA 见同名 `inputs-789f.json` 与 `interface-789f.md`。

| 实际阶段 | 结果 | elapsed 秒 | 峰值 KiB | raw bytes / SHA-256 |
|---|---|---:|---:|---|
| inspect 30 秒预算 | exit 0；投影秩 14，19404 原组合产品真 | 0.30454507999820635 | 20564 | 1643 / `89ffea5cf5d6801eb0f8a88178475f7857e0ed4acc4d3ae0ec00d04a2975f020` |
| final 120 秒预算 | exit 0；全部十四个原十/十八换源产品真 | 20.885148269997444 | 138168 | 5966 / `db5da541150a13906ad9ee639ae205121ffd29708e9d954ee1bf9095a9116a4d` |

同一 binding 为

~~~text
6d4cae67816b6de0e3fd41bc1033cf15b5b70d000d8aef5cee122df473bf7da8
~~~

final manifest 为 5484 bytes / SHA-256 `618bbbc841ead87162e068543a325e437b38e22020855e8b475207bb7ab57988`。它记录全部 16 个完整阶段的物理与逻辑 SHA：一个完整小投影、十四个完整原换源和一个最终证书。最终证书为 500 bytes / SHA-256 `ce99c911c8896c70ef78889e68ffe4b305982c73d0e1d106b34c56d42cdee76d`；逻辑数据为 1289 bytes / SHA-256 `094cff596268e6eeb2b9d894b52ff1bfb59bc44160e5c0744778c41dac95bb6c`。

两阶段执行身份位于 `notes/r150-original-parameter-module-execution-789f/` 下的 `local-20261116-weight8-old-high-source-exchange127-inspect30.json` 和 `local-20261116-weight8-old-high-source-exchange127-final120.json`。后者列明全部阶段身份，不保存数学数组。所有完整关系、来源多项式、raw 和缓存只保留在临时目录。

## 8. 根的完整审读与回读

根全文审读冻结消费者、输入清单及接口，逐核小投影的原七十四维变换、全部 19404 组合坐标、选中目标范围和十四条原十/十八多项式终门。另独立回读全部十六阶段的物理与逻辑 SHA、完整 raw 和 manifest，并重算同一语义 binding；均与上述实际身份一致。最小稳定闭包的两个包含和完整第一轮的三类全部像已另作直接代数核验。此复核不增加未付的稳定停止或特征零断言。
