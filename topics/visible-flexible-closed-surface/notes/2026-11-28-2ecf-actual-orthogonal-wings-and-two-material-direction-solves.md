# 两种新双翼真端口的整场与各自固定度量实际求解

**数值证据。**

在相同中央 R267、相同 .115 真喉和固定帽源上，取 R288 真实新端口，短轴幅 .85 保持。分别用 65 条真实空间极角径线对正、负长翼做端速度/位置求解，再构成覆盖所有材料角的实际 Fourier–Hermite 曲面，并计算各自完整 G10/G11。
从各自刚构造的整场独立开始，以相同冻结 11 个半径系数的目标 g，分别在真实材料角上解 575 个球向位置参数和各 u 的三维积分位移闭合乘子。每个新输入均有自身 250 次接受；向上的长翼在该次优化后出现独立网曲率逾十万。四张场都由各自输出 NPZ 和准确端口函数定义。

| 长翼幅 | 物理极角曲面 G11 误差 / κ / held | 真实材料方向优化后 G11 |
|---:|---|---|
| 0.35 | 1.557339636 / 15.50585963 / 0.6488351708 | 1.29625021 / 103134.0359 / 0.6255506842 |
| -0.35 | 1.557214971 / 15.50585921 / 0.6488351353 | 0.2069466843 / 12.73417503 / 0.6261330179 |

## 可移植重生

W 是已有相应输入的运行目录，S 是课题公开 scripts 的绝对路径。每条命令按列出的输入和输出文件生成自己的实际状态。

```sh
cd "$W"
export OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 OMP_NUM_THREADS=1
python3 -u "$S/2ecf-polar-orthogonal-disjoint-wing-developable-port.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --amplitude .35 --flat .85 --field polar-orthogonal-wings-up.npz --output polar-orthogonal-wings-up.json
python3 -u "$S/2ecf-polar-orthogonal-disjoint-wing-developable-port.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --design polar-orthogonal-wings-up.json --field polar-orthogonal-wings-up.npz --trace-nodes 2048 --output polar-orthogonal-wings-up-full.json
python3 -u "$S/2ecf-polar-orthogonal-wing-two-material-port-solve.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-orthogonal-wings-up.json --seed-field polar-orthogonal-wings-up.npz --start polar-gap092-material-implicit-frozen11.json --frozen polar-gap092-material-implicit-radius11.json --iterations 250 --field polar-orthogonal-wing-material-up.npz --output polar-orthogonal-wing-material-up.json
python3 -u "$S/2ecf-polar-orthogonal-wing-two-material-port-solve.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-orthogonal-wings-up.json --design polar-orthogonal-wing-material-up.json --field polar-orthogonal-wing-material-up.npz --output polar-orthogonal-wing-material-up-full.json
python3 -u "$S/2ecf-polar-orthogonal-disjoint-wing-developable-port.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --amplitude -.35 --flat .85 --field polar-orthogonal-wings-down.npz --output polar-orthogonal-wings-down.json
python3 -u "$S/2ecf-polar-orthogonal-disjoint-wing-developable-port.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --design polar-orthogonal-wings-down.json --field polar-orthogonal-wings-down.npz --trace-nodes 2048 --output polar-orthogonal-wings-down-full.json
python3 -u "$S/2ecf-polar-orthogonal-wing-two-material-port-solve.py" --mode design --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --seed-design polar-orthogonal-wings-down.json --seed-field polar-orthogonal-wings-down.npz --start polar-gap092-material-implicit-frozen11.json --frozen polar-gap092-material-implicit-radius11.json --iterations 250 --field polar-orthogonal-wing-material-down.npz --output polar-orthogonal-wing-material-down.json
python3 -u "$S/2ecf-polar-orthogonal-wing-two-material-port-solve.py" --mode observe --scripts "$S" --ramp polar-new-gap-092-master-ramp.npz --coast polar-new-gap-092-master-coast.npz --prepared polar-new-gap-092-prepared.json --independent polar-new-gap-092-independent.json --seed-design polar-orthogonal-wings-down.json --design polar-orthogonal-wing-material-down.json --field polar-orthogonal-wing-material-down.npz --output polar-orthogonal-wing-material-down-full.json
```

## SHA256

| 原件 | SHA256 |
|---|---|
| 2ecf-polar-orthogonal-wing-two-material-port-solve.py | 3317bb71e0bedac8c17f897b7a9ba536af8d57463aacc6ec92b16bb6a5036d9e |
| polar-orthogonal-wings-up.json | 44011c3ca8dc426a2f65facf97022043e1549e384549879e710d8edfc0b09616 |
| polar-orthogonal-wings-up.npz | 8252c6b2ca80de8341bb5af6a47f1d142caf6f3532b45f06da0e3cafd5839a10 |
| polar-orthogonal-wings-up-full.json | 2a4a78bf2320cb286fe9837e1ee75c2495fe15761a9d88a5eed462205911ca83 |
| polar-orthogonal-wing-material-up.json | 232630dfb6315d47ab455a0674308fc43d822252b5ef601c0a43194677490f85 |
| polar-orthogonal-wing-material-up.npz | 9966fb831748622d7cb6469cee24c2ec8a0df1820cce64bc4b63eead05ae372a |
| polar-orthogonal-wing-material-up-full.json | dd4631d4351d324866b9dc920327bdaaf9efdef2afc384ff4ed41d24d89c85e4 |
| polar-orthogonal-wings-down.json | 82cefb18741e12722d357b84ff4c93830db9d4848cb8f448acf4fecf444af66a |
| polar-orthogonal-wings-down.npz | f8498fb8fcf3e8110793365e09eec1b8243eacdf31a4f52ff991b00ea6273a12 |
| polar-orthogonal-wings-down-full.json | 0642b1a8293e812a22326dc92e9ca5be49664893b5215b451ba46a1c532c7b88 |
| polar-orthogonal-wing-material-down.json | 120863f03e4a44935a5729a6e4c7c902ea1ee37d63c1e073d65325b26b4e2e8f |
| polar-orthogonal-wing-material-down.npz | bacbeb5ec9a7e70d6fafe989d2e8c74d38cbb234bd07ee7078f88d04f4124fcc |
| polar-orthogonal-wing-material-down-full.json | d9dbd24d3d5bc0a7001c82ab941392e6973c0ded19a3fdc949de74cc5bb9dfc7 |
| polar-orthogonal-wings-up-exit.json | 85c988d2a967e3d5d6c9252faa64f03f4b1b0d22d68b645a453046cec6af72b6 |
| polar-orthogonal-wings-up.log | 98ae05a87588b3e45ba211ef37f7c0b2fab81e0e11812d353168776f31406038 |
| polar-orthogonal-wings-up-full-exit.json | a316ac87a331b2e434aac2a84c63e64ee63ab0818ebb83a757c24ed6916b9e21 |
| polar-orthogonal-wings-up-full.log | bf4f3b92d531b857c5b69c494dc41fa2ed507af657d7507e36337dca7b197492 |
| polar-orthogonal-wing-material-up-exit.json | a372cb044cacbd1765040327e669094e252aee559b520fdecd5ae536f5df41bd |
| polar-orthogonal-wing-material-up.log | d2bd2094a1e29de6f443c9ae9ed9d743d6b7ed9212f39f2710bdd2f5fa84a044 |
| polar-orthogonal-wing-material-up-full-exit.json | 04cc6defac984c8f385d17fe4a5ae06a0de2df48379d15b27a3d482d0546d04d |
| polar-orthogonal-wing-material-up-full.log | 2e2180ae9527621a79f71b187a7c64006fdcd607065f605319ad9586bcea4c4b |
| polar-orthogonal-wings-down-exit.json | 897b71977beb7510680d25cbc27ee633b5ddfa9e08bac6bd2750cbabd583ae25 |
| polar-orthogonal-wings-down.log | 545e83cf6525e65652284f287294957aa23af58151e75d45519c2d43117f2cf7 |
| polar-orthogonal-wings-down-full-exit.json | a558a60045dbcb2979955895913c9b3c0ffc1886821349635d2c4092edf93a76 |
| polar-orthogonal-wings-down-full.log | 52b5fbdc91ba909ad09773c653d08e238eee59ef8cc7e428dded13a4610a6bc5 |
| polar-orthogonal-wing-material-down-exit.json | a00418452e1c632c3d5bf813f1483c52e9a744303be28de41de539d458889562 |
| polar-orthogonal-wing-material-down.log | fdede70b792df9b67dd580bd23f1cb85066d0ccb66fa108e97a44e08144993be |
| polar-orthogonal-wing-material-down-full-exit.json | adad76be81e4bd53a588b8f5629d22767b82e2b5e3706293a4b517521120a552 |
| polar-orthogonal-wing-material-down-full.log | e1c8e07387be5f41d04f1a56363b9455701f9468995ecb67d592bd6b5c152b25 |
