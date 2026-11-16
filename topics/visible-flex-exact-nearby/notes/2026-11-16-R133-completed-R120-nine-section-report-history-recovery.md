# R120 完成九截面报告的历史恢复

2026-11-16。按根README第15条，用普通提交删除两份已经完成、由保留脚本产生的派生报告；不改写历史，不删除候选定义、原输入、证明、脚本、依赖清单、失败前缀或连续首格报告。新科学计算仍只用公开仓库自身Actions。此清理没有执行任何旧科学目标。

## 精确恢复对象

下列完整文件均可从公开不可变提交 93eb013259ae836de5de23e80873744493e10cef 的同一路径恢复。当前与该恢复点的Git blob/bytes相同；SHA256逐字来自保留的R120完整依赖清单。大报告正文没有经connector读取，也没有声称重新计算其SHA。

| 完整仓库路径 | Git blob | 字节 | 原记录SHA256 |
|---|---|---:|---|
| topics/visible-flex-exact-nearby/notes/2026-11-13-newton-source-centered-mean-nine-radii-native.json | 75893162c78e1f7e058166857ec22fb43f69bd67 | 258275 | 936714458505604a7df74a7e50dc1e455d5bfb5676a6206f6076a3a62d93e8f9 |
| topics/visible-flex-exact-nearby/notes/2026-11-13-newton-source-initial-nine-radii-native.json | 68a2a048debe581cead035006385bcd23b4d50ab | 251668 | 96810b7997f7cdd5996d908cb9355066966e081bfa5fdd799f19b7175a769a8f |

两件共509943字节。恢复应先用git show取同一原文件，再在本地或Actions核完整字节、Git身份和原SHA；不得为恢复而重跑producer。完整报告首部的object/origin/direction身份、准确中心和参数分数、原行序与所有记录随原字恢复，不能由报告文件名补造。

## 完成证据、源码与原参数

保留的 results/R120-centered-Fourier-Newton-source.md 为完整证明，Git fb2b688a758403f2544ee7b9bbadf865588c050e，8509字节。
保留的 notes/2026-11-13-R120-newton-source-native-manifest.json 为完整递归依赖及 completed_native_reports 表，Git ae9a64033a61dfa9a83e99a6aa43e0a2143eae07，5377字节，SHA256 ba5d632eb9b6e6799999c4524d0e73d90288199ed3c4c12a9fd2d1b35dca5522。表中这两个路径被列为已完成原生报告，不是失败输出。

两个保留producer均已完整按文本读取，其当前字节SHA与该原清单相同：

| 程序 | Git blob | 字节 | SHA256 |
|---|---|---:|---|
| scripts/fourfold_phase_newton_source_centered.py | eb1277680921c2cbfd772c5e158eec4cb0cb51cd | 6195 | 1bb36ce8ef6e8043f76c648b005cc3f56609e97ec49852f36bdbda80a5e4749d |
| scripts/fourfold_phase_two_jet_newton_source.py | 0d1d4c5f606caa7aaf7500ceac67d6e8a704b410 | 21116 | cd7c36692b48844d268dc87e20556e39a869da154ce5e3826a6bdc0b50162f2a |

中心化入口调用同一旧源的main，仅用完整Wiener误差组织替换多项式包络；其输出kind和centered_convolution_source_sha256明确区别于原入口。两者都保留真实mean、整个primitive尾、同一固定初始目标和原参数盒。源程序的完成标记只在所有指定径向行保存后置真。

R120明确记录中心化九点命令为：

```sh
python scripts/fourfold_phase_newton_source_centered.py \
  --points 0 1/8 1/4 1/2 1 3/2 2 5/2 3 \
  --out notes/2026-11-13-newton-source-centered-mean-nine-radii-native.json
```

这是原执行身份说明，不是现在应执行的命令。默认object为 data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json，参数半宽1/10^9、primitive nodes512、Arb192bits，乘积网格4096及全角连续cover。准确原对象哈希和实际参数仍以历史原报告首部为准。原入口九点报告的完整原调用与每行参数通过其历史原文件保留；本清理不从文件名猜造运行记录。

原执行属于2026-11-13的原生Python/Arb阶段，清单记录Python3.12.14/python-flint0.9.0；不将其重新标为2026-11-16的公开Actions运行。R120记录中心化九截面36.85秒、另一个保留的连续首格8.94秒。没有补造未记载的Actions run编号。

## 原结论范围和所有限制继续有效

R120的九个径向截面是0、1/8、1/4、1/2、1、3/2、2、5/2、3；每个截面覆盖全实物理角和同一完整参数盒，并支付完整primitive无穷尾。它们是径向点域，不覆盖整个径向区间，不提供复角strip或强Sobolev结论。

证明表逐项保留新的源/材料源/度量C1界以及原入口比较：在r=1/8、1/4旧源上界508.552、744.697，新中心化界约0.116、0.0674。新的r=0源界约0.630432仍不能当作Newton收敛门。没有删去源的常数mean或重新选择目标。

连续首格报告 notes/2026-11-13-newton-source-centered-first-germ-native.json 保持原位；它给出的约966319源界仍不能授非线性小量。另两个原生报告、recovered metric报告、全部对象/源/源依赖清单也保留。新的完成状态不扩至全闭曲面、完整PDE强逆、更新邻域或非线性族。

未来任何消费者若依赖删除的原报告，应按本页准确提交/路径/完整身份临时恢复；不得复用摘要数字替代完整数学域，也不得重算已成功的旧目标。先前清理中对“native”的排除仅是那些单次清理的范围，不构成根规则15之外的永久禁删规则。
